
__version__ = "0.9"
__author__ = "Thomas Baldauf"
__email__ = "thomas.baldauf@dlr.de"
__license__ = "MIT"
__birthdate__ = '15.11.2021'
__status__ = 'prod' # options are: dev, test, prod


from ..core.settings import Settings
from ..bottomup.stock_manager import StockManager
from ..core.flow_matrix import FlowMatrix

import pandas as pd
import warnings
import numpy as np
from collections import defaultdict
from enum import Enum
import copy


class BalanceEntry(Enum):
    """
    these are the different entry types
    """
    ASSETS = 0
    EQUITY = 1
    LIABILITIES = 2
    TOTAL = 3


class BankruptcyEvent(Enum):
    """
    bankruptcy cases
    """
    NEGATIVE_ASSETS = 0
    NEGATIVE_LIABILITIES = 1
    NEGATIVE_EQUITY = 2


class BalanceSheet:
    """
    This is the balance sheet of an agent (it could be used as a standalone datastructure, too, in theory). A balance sheet is of the following form

+------------------+-------------------------+
|    ASSETS        | LIABILITIES AND EQUITY  |
+==================+=========================+
|                  |                         |
|   ...            |   Liabilities           |
+------------------+-------------------------+
|                  |   ...                   |
+------------------+-------------------------+
|                  |   Equity                |
+------------------+-------------------------+
|                  |   ...                   |
+------------------+-------------------------+
|TOT ASSETS     = TOT LIABILITIES AND EQUITY |
+--------------------------------------------+

    more information can be found here https://www.investopedia.com/terms/b/balancesheet.asp for example.

    """

    _tolerance = 1e-6 # tolerance for engage()
    _tolerance_rel = 1e-4 # relative tolerance of deviation from total assets

    @classmethod
    def change_tolerance(cls, tol:float, rel_tol:float):
        """
        Change the tolerance by which the balace is allowed to diverge
        This will set the new values globally. The tolerance is checked in a two-step process:
        Frist, the absolute tolerance violation is checked, i.e. if any balance sheet side sums up to more or less than the other side.
        If the absolute tolerance is violated, an error is thrown if also the relative tolerance is exceeded. The latter is the second step of the checking process.
        If the relative deviation is violated but the absolute level is not exceeded, no error wil be thrown.

        :param tol: new absolute tolerance
        :param rel_tol: relative tolerance (relative devaition from total assets)
        """

        assert tol > 0
        cls._tolerance = tol
        cls._tolerance_rel = rel_tol

    class Proxy:
        """
        Proxy class for balance sheet. It can be either engaged (consistent and 'active') or disengaged (inconsistent and 'disabled').
        The consistency is automatically checked inside the 'engage()' call when switched from disengaged to engaged.
        """
        def __init__(self, parent):
            self.parent = parent

        def __enter__(self):
            self.parent._engaged = False # disengage()

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.parent.engage()
            self.parent._engaged = True # engage()

    def __init__(self, owner):
        """
        Balance sheet constructor. Creates a new balance sheet

        :param owner: the owner agent of this balance sheet. Can be None for standalone purposes, but it is recommended to pass an Agent instance here.
        """
        self.owner = owner # stores owner instance, if any
        default_value = 0.0 # np.nan NOTE if nan is set this can lead to misbehavior in engage.
        self._sheet = defaultdict(lambda: {BalanceEntry.ASSETS: default_value,
                                          BalanceEntry.EQUITY: default_value,
                                          BalanceEntry.LIABILITIES: default_value}) # the actual data structure is a three-column table for assets, equity and liabilities

        self._sheet[BalanceEntry.TOTAL] = {BalanceEntry.ASSETS: default_value,
                               BalanceEntry.EQUITY: default_value,
                               BalanceEntry.LIABILITIES: default_value} # the 'total' row at the bottom

        self._engaged = True  # <- this can deactivate the consistency check temporarily for modification. Manual modification is not allowed (therefore private).
        self._bankrupt = False # <- this stores if the owner went bankrupt. manual modification should not be needed (therefore private).
        # self.tolerance -> self.__class__.tolerance # numerical tolerance for consistency cross-check

        # link agents to specific entries in the balance sheet
        # nested by [BalanceEntry]->[ItemName]->[Agent]->[float Balance]
        self._changelog = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: 0.0)))

    def add_changelog(self, agent, name, which, x):
        """
        inserts a link between a specific balance sheet item to a
        for example, a bank might want to record which agent its deposits belong to...
        Data structure: [BalanceEntry]->[ItemName]->[Agent]->[float Balance]

        :param agent: agent instance to store here
        :param name: name of the item, e.g. 'Deposits'
        :param which: corresponding BalanceEntry
        :param x: quantity which is inserted, can be positive, zero or negative
        """
        # assert isintance(x,int) or isinstance(x,float), "wrong data type"
        y = self._changelog[which][name][agent]

        if np.isnan(y):
            self._changelog[which][name][agent] = x  # first time this is called? overwrite nan
        else:
            self._changelog[which][name][agent] = x + y # after first time

    @property
    def raw_data(self):
        """
        get the raw data of this data structure in dictionary format.
        This will create a copy of the original data, so the user won't operate on the data directly (which is forbidden)
        """
        d = copy.deepcopy(self._sheet) # deep copy because its a nested dict TODO compress the data somehow
        del d[BalanceEntry.TOTAL]
        return d

    def get_last_changelog(self, name, which,agent=None):
        """
        returns the internally stored links to other agents made via balance sheet transactions

        :param agent: agent instance to store here. if None, all agents' entries will be returned
        :param name: name of the item, e.g. 'Deposits'
        :param which: corresponding BalanceEntry
        :return: float, current balance or dict of balances for agents
        """

        if agent is not None:
            return self._changelog[which][name][agent]
        return self._changelog[which][name]

    #def items(self):
    #    return self.raw_data.items()

    #def values(self):
    #    return self.raw_data.values()

    #def keys(self):
    #    return self.raw_data.keys()

    def __repr__(self):
        return "<Balance Sheet of %s>" % self.owner

    def __str__(self):
        return self.__repr__()

    def __getitem__(self, key):
        """
        Get an entry of the balance sheet
        :param key: str, name of the asset
        :return: a dict with ASSETS, EQUITY, LIABILITIES entries of this item in this particular agent. NOTE In most cases, at least 2 of the entries will be zero.
        """
        return self._sheet[key]

    @property
    def modify(self):
        """Modification decorator. Temporarily disengages the data structure. This can be used in a with block:

        .. code-block:: python

            with balance_sheet_1.modify:
                with balance_sheet_2.modify:
                    balance_sheet_1.change_item(...)
                    balance_sheet_2.change_item(...)

        """
        return self.Proxy(self)

    def restore_after_bankrupcy(self,verbose=False):
        # helper function to reset bankrupt flag to False again after bankruptcy has been fixed (e.g. replacement of agent by new fictitious entrant)
        if verbose:
            warnings.warn("%s restore after bankrupcy" % self.to_string()) # TODO < test this

        self._bankrupt = False

    def disengage(self):
        """
        'unlocks' the balance sheet -> can be modified now without error
        """
        self._engaged = False

    def engage(self):
        """
        locks the balance sheet -> no longer can be modified
        performs also a cross-check if consistency is maintained
        """

        eps = self.__class__._tolerance # tolerance level for cross-check, 1e-6 by default

        a = 0.0 # dummy for sum of entries
        e = 0.0
        l = 0.0

        # iterate through the rows of the balance sheet and sum up assets, liabilities, equity
        for entry, data in self._sheet.items():

            if entry == BalanceEntry.TOTAL:
                continue

            a_i = data[BalanceEntry.ASSETS]
            e_i = data[BalanceEntry.EQUITY]
            l_i = data[BalanceEntry.LIABILITIES]

            a += a_i
            e += e_i
            l += l_i

            if a_i < -eps: # handle negative assets

                if True: #  TODO might add exceptions for some special cases?
                    if not self._bankrupt:
                        self._bankrupt = True
                        warnings.warn("filed bankruptcy for %s\n" %self.owner)
                        self.owner.file_bankruptcy(event=BankruptcyEvent.NEGATIVE_ASSETS)

                    return None

                else: # NOTE not used as of now...
                    s = self.to_string()
                    error = ValueError("%s of %s reached a value below zero after engage() call" % (entry, self.owner) + "\n\n" + s)
                    raise error

            if l_i < -eps: # handle negative liabilities

                if True: #  TODO might add exceptions for some special cases?
                    if not self._bankrupt:
                        self._bankrupt = True
                        warnings.warn("filed bankruptcy for %s\n" %self.owner)
                        self.owner.file_bankruptcy(event=BankruptcyEvent.NEGATIVE_LIABILITIES)

                    return None

                else: # NOTE not used as of now...
                    s = self.to_string()
                    error = ValueError("%s of %s reached a value below zero after engage() call" % (entry, self.owner) + "\n\n" + s)
                    raise error

        if abs(a - (e+l)) > eps: # check bookkeeping equation for consistency within tolerance level eps

            # almost zero? bookkeeping equation obeyed
            eps2 = self.__class__._tolerance_rel # relative tolerance
            if a !=0 and abs(a - (e+l))/abs(a) < eps2:

                pass
                # relative deviation is still small?  -> just warn
                # warnings.warn("balance sheet of %s is numerically instable. Deviation %.10f" % (self.owner, a-(e+l)) + "\n\n" + s)
                # NOTE ^ above code was commented out because no case could be thought of where this would make sense.

            else: # not almost zero? bookkeping equation violated
                s = self.to_string()
                error = ValueError("balance sheet of %s is corrupted after cross-check. Deviation %.10f" % (self.owner, a-(e+l)) + "\n\n" + s)
                raise error

        if e < 0 and e < -eps: # negative equity? = 'balance sheet under water'

            if not self._bankrupt:
                self._bankrupt = True
                self.owner.file_bankruptcy(event=BankruptcyEvent.NEGATIVE_EQUITY)
            else:
                # already bankrupt -> do not trigger bankruptcy a second time... # TODO < think about logic in here
                pass
            return None

    def get_balance(self, key, kind=BalanceEntry.ASSETS) -> float:
        """
        Gets amount of a certain entry for certain key

        :param key: name of entry (e.g. 'Cash' or 'Apples')
        :param kind: preferrably BalanceEntry: Asset, Liabilities or Equity, optionally str 'Assets', 'Equity' or 'Liabilities'

        :return: float, value in balance sheet
        """

        # TODO automatically detect which kind it is if the other two are zero(?) instead of default value being ASSETS

        if isinstance(kind, str):
            mydict = {
                "Assets": BalanceEntry.ASSETS,
                # BalanceEntry.ASSETS: BalanceEntry.ASSETS,
                "Equity": BalanceEntry.EQUITY,
                # BalanceEntry.EQUITY: BalanceEntry.EQUITY,
                "Liabilities": BalanceEntry.LIABILITIES,
                # BalanceEntry.LIABILITIES: BalanceEntry.LIABILITIES,
            }
            which = mydict[kind]
        else:
            which = kind # should be BalanceEntry at this point! Will raise KeyError if not

        if not which in self._sheet[key]:
            raise KeyError("Could not find entry for %s"% which)

        return_value = self._sheet[key][which]

        if np.isnan(return_value): # nan values are not allowed, so throw an error
            msg = "Requested Value is NaN (not a number)."
            raise RuntimeError(msg)

        return return_value

    def to_string(self):
        """
        Coverts the whole balance sheet to a pandas dataframe and subsequently to a string

        :return: str, balance sheet string representation
        """
        # TODO think of different graphical representations, e.g. entries in rows instead of columns
        return "\n\n" + self.to_dataframe().to_string().replace("NaN"," ~ ") + "\n\n"

    def change_item(self, name, which, value, suppress_stock=False):
        """
        Chanes value of an item in the balance sheet.

        :param name: name of the asset / entry to change
        :param value: value is added to entry. can also be negative
        :param which: BalanceEntry: Asset, Liability, Equity
        """

        if value == 0:  # security lock if this is a 'ghost transaction'
            warnings.warn("Blocked ghost item in balance (value=0): %s, %s,%s,%s"% (self,name,which,value))
            return

        if self._engaged: # security lock when balance is still disengaged
            raise PermissionError("Cannot change item in engaged balance sheet! This would lead to inconsistencies. Please disengage before calling change_item or use 'modify' proxy.")

        if np.isnan(self._sheet[name][which]):
            warnings.warn("Found NaN value in %s, %s, %s" % (self,name,which))
            # self._sheet[name][which] = 0 # NOTE <- alternative way to handle

        if np.isnan(self[BalanceEntry.TOTAL][which]):
            warnings.warn("Found NaN value in %s, %s, %s" % (self,"TOTAL",which))
            # self._sheet[BalanceEntry.TOTAL][which] = 0 # NOTE <- alternative way to handle

        self._sheet[name][which] += value
        self._sheet[BalanceEntry.TOTAL][which] += value

        if not suppress_stock:
            # Suppresses logging in the transaction flow matrix. This can be helpful in some cases

            if which == BalanceEntry.ASSETS:
                FlowMatrix().capital_flow_data["Δ %s" % name][self.owner] += -value #-value
            if which == BalanceEntry.LIABILITIES:
                FlowMatrix().capital_flow_data["Δ %s" % name][self.owner] += value #value

            if which == BalanceEntry.EQUITY and name == "Cash":
                raise ValueError("Cash cannot be equity")


    """
    TODO (?) insert operations like 'Aktivtausch', 'Passivtausch', 'Bilanzverlängerung'(?)
    """

    def to_dataframe(self):
        """
        Create a dataframe from this data structure. Warning: this is computationally heavy and should not be used in loops!

        :return: pandas dataframe
        """

        df = pd.DataFrame({"Entry": [],"Assets": [], "Equity": [],"Liabilities": []}) # construct an empty 'dummy' data frame
        entries = [] # allocate list of commodities entered in the balance sheet

        null_sym = "   .-   " # symbol for zero entries

        # iterate through the balance sheet items and 'fill the table'
        for key, row in self._sheet.items():

            if key != BalanceEntry.TOTAL: # consider all rows except the 'total' entry
                entries.append(key) # add to entries list
                new_row = pd.DataFrame({"Entry": [key],
                                        "Assets": [row[BalanceEntry.ASSETS]],
                                        "Equity": [row[BalanceEntry.EQUITY]],
                                        "Liabilities": [row[BalanceEntry.LIABILITIES]]}) # construct a new row
                df =  pd.concat([df,new_row.replace(0.0,null_sym)])

        df = df.sort_index() # sort the entries by index

        # Compute 'Total' row
        # dummy for modifying factors.
        # NOTE is 1 always for now, but might change with exchange rates or any other conversion factors (?)
        factors = [1.0 for key in entries]
        my_row = pd.DataFrame({"Entry": ["Total"],
                                "Assets": [np.dot(df["Assets"].replace(null_sym,0.0),factors)],
                                "Equity": [np.dot(df["Equity"].replace(null_sym,0.0),factors)],
                                "Liabilities": [np.dot(df["Liabilities"].replace(null_sym,0.0),factors)]})
        df = pd.concat([df,my_row]) # adds the 'Total' row

        df = df.set_index("Entry") # sets index column correctly
        df.index.name = "BALANCE SHEET OF %s" % self.owner # gives the balance sheet an understandable title

        return df

    def depreciate(self):
        """
        (BETA) this will look up all the required depreciation rates in the
        settings and depreciate the balance sheet.
        Equity will become less, liabilities will stay.
        """

        settings = Settings() # read depreciation rates from settings

        for item_name in self._sheet.keys():

            depr_rate = settings.config_data["params"][item_name]["depreciation"]
            # Settings entry is 'param->(item name)->depreciation->value'

            depr_q = self._sheet[item_name][BalanceEntry.EQUITY] * depr_rate
            # Warning: Depreciation is percentage of current stock. Non-linear!

            if not np.isnan(self._sheet[item_name][BalanceEntry.EQUITY]):
                self._sheet[item_name][BalanceEntry.EQUITY] -= depr_q

            if not np.isnan(self._sheet[item_name][BalanceEntry.ASSETS]):
                self._sheet[item_name][BalanceEntry.ASSETS] -= depr_q

        # TODO maybe automatically log this on income statement of the underlying agent here?

    @property
    def leverage(self) -> float:
        """
        computes the financial leverage value (debt-to-assets ratio)
        of this balance sheet

        .. math::
            Leverage = LIABILITIES / (LIABILITIES + NET WORTH)

        :return: float, leverage
        """

        E = self.net_worth
        L = self.total_liabilities

        if E + L == 0:
            return np.inf

        lev = L / (E+L)

        return max(0,lev)

    @property
    def net_worth(self) -> float:
        """net worth = sum of equity
        """
        return_val =  self._sheet[BalanceEntry.TOTAL][BalanceEntry.EQUITY] #"Equity"]
        if np.isnan(return_val):
            return 0.0
        return return_val

    @property
    def total_assets(self):
        """
        total assets = sum of assets column
        """
        return_val = self._sheet[BalanceEntry.TOTAL][BalanceEntry.ASSETS] # "Assets"]
        if np.isnan(return_val):
            return 0.0
        return return_val

    @property
    def total_liabilities(self):
        """
        total liabilities = sum of all liabilities in liability column
        """
        return_val = self._sheet[BalanceEntry.TOTAL][BalanceEntry.LIABILITIES] # "Liabilities"]
        if np.isnan(return_val):
            return 0.0
        return return_val


    def plot(self,show_labels=True,cols_assets=None, cols_liabs=None,cols_eq=None,show_legend=True,
                  fname=None,ax=None):
        """
        creates a matplotlib plot of the balance sheet

        :param show_labels: show labels (numbers) above the bars
        :param show_legend: (True) show a legend with the balance sheet entries

        By default, assets are red, equity is blue and liabilites are green
        but custom colors can be given

        :param cols_assets: (None) list of mpl colors for assets
        :param cols_liabs: (None) list of mpl colors for liabilities
        :param cols_eq: (None) list of mpl colors for equity

        if you want to save to file instead of showing as plot window, specify a fname
        :param fname: if None (default) is given, plot will be shown directly. If fname is given, plot will be saved to a file


        if you want to redirect the plot to a certain axis, you can enter the axis via the parameter ax
        :param ax: axis to plot on. setting this parameter different from None will make 'fname' ineffective
        """
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        from ..misc.mpl_plotting import matplotlib_barplot

        balance_sheet = self

        title = "%s" % balance_sheet.owner

        assets = []
        liabilities = []

        colors = []

        if cols_liabs is None:
            greens = [ "lightgreen", "honeydew","seagreen", "darkgreen", "darkslategray"]
        else:
            greens = cols_liabs

        if cols_eq is None:
            blues = ["lightsteelblue", "lavender", "powderblue", "steelblue", "royalblue", "blue"]
        else:
            blues = cols_eq

        if cols_assets is None:
            reds = ["salmon", "indianred", "rosybrown", "orangered", "red", "indianred"]
        else:
            reds = cols_assets

        greens.reverse()
        blues.reverse()
        reds.reverse()

        # color patches for legend
        legend_patches = []
        blue_patches = []
        green_patches = []
        red_patches = []

        # data for plotting
        data = {"Assets": [], "Liabilities & Equity": []}
        labels = {}
        i = 0

        assets = []
        lia = []
        equi = []

        # construct data for plotting
        for key, val in balance_sheet._sheet.items():

            if key != BalanceEntry.TOTAL:

                if val[BalanceEntry.LIABILITIES] != 0.0:  # is liability

                    # data["Assets"].append(0.0)
                    # data["Liabilities & Equity"].append(val["Liabilities"])
                    assets.append([key, 0.0])
                    lia.append([key, val[BalanceEntry.LIABILITIES]])

                if val[BalanceEntry.EQUITY] != 0.0:  # is Equity

                    # data["Assets"].append(0.0)
                    # data["Liabilities & Equity"].append(val["Equity"])

                    assets.append([key, 0.0])
                    equi.append([key, val[BalanceEntry.EQUITY]])

                if val[BalanceEntry.ASSETS] != 0.0:  # is Asset

                    # data["Assets"].append(val["Assets"])
                    # data["Liabilities & Equity"].append(0.0)

                    assets.append([key, val[BalanceEntry.ASSETS]])
                    lia.append([key, 0.0])

        # construct data for plotting
        # by default, assets are red, equity is blue and liabilites are green
        k = 0
        for a in assets:

            key = a[0]
            val = a[1]

            if val != 0:
                data["Assets"].append(val)
                data["Liabilities & Equity"].append(0.0)

                col = reds[k%len(reds)]
                colors.append(col) # (col, "black"))
                red_patches.append(mpatches.Patch(color=col, label=key))

                labels[i] = key
                i += 1

            k+=1


        k = 0
        for e in equi:
            key = e[0]
            val = e[1]

            if val != 0:
                data["Assets"].append(0.0)
                data["Liabilities & Equity"].append(val)

                col = blues[k%len(blues)]
                colors.append(col) # ("black", col))
                blue_patches.append(mpatches.Patch(color=col, label=key))

                labels[i] = key
                i += 1

            k+=1

        k = 0
        for l in lia:

            key = l[0]
            val = l[1]

            if val != 0:
                data["Assets"].append(0.0)
                data["Liabilities & Equity"].append(val)

                col = greens[k%len(greens)]
                colors.append(col) #("black", col))
                green_patches.append(mpatches.Patch(color=col, label=key))

                labels[i] = key
                i += 1

            k+=1

        # create customized patche for the legend
        legend_patches = red_patches + blue_patches + green_patches

        df = pd.DataFrame(data).T
        df = df.rename(columns=labels).T

        # print("PLOT\n",df)
        # print("colors",colors)



        fig = matplotlib_barplot(df.T, xlabel="", ylabel="", color=colors, title=title, stacked=True, show_labels=show_labels,fmt="{0:.2f}",
                                legend="off", size=(4, 4), show=False,ax=ax)

        if ax is None:
            ax = plt.gca()

        ax.legend(handles=legend_patches, bbox_to_anchor=(1.3, 1),framealpha=0.0)

        plt.axis("off")
        plt.tight_layout()

        if ax is None:
            if fname is None:
                plt.show()
            else:
                plt.savefig(fname)
                plt.close()

        return ax 

    @classmethod
    def plot_list(cls,list_of_balance_sheets,dt=1,xlabel=None,ylabel=None,title=None,show_liabilities=True,show=True):
        """
        Plots a list of balance sheets (e.g. a collected temporal series)

        :param list_of_balance_sheets: a list of BalanceSheet instances
        :param dt: step, (how many values to skip in between)
        :param xlabel: x axis label
        :param ylabel: y axis label
        :param title: title of the figure
        :param show_liabilities: boolean switch to show passive side of balance sheet as downward-pointing bars (default True)
        :param show: show the plot in a new window? if False, only the matplotlib figure is returned
        """
        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        from ..misc.mpl_plotting import matplotlib_barplot

        entries = {}

        for data_i in list_of_balance_sheets:

            # print("DATA_I",data_i)
            #print("\n\n --\n\n")

            for k,v in data_i.items():

                if k not in entries:
                    entries[k] = {}

                for k2, v2 in v.items():

                    if k2 not in entries[k]:
                        entries[k][k2] = []

                    if not np.isnan(v2):

                        if k2 == BalanceEntry.ASSETS:
                            if np.abs(v2) > 0.0:
                                entries[k][k2].append(np.abs(v2))
                        else:
                            if show_liabilities:
                                if np.abs(v2) > 0.0:
                                    entries[k][k2].append(-np.abs(v2))


        # print("ENTRIES",entries)


        plt.figure()

        if xlabel is not None:
            plt.xlabel(xlabel)
        if ylabel is not None:
            plt.ylabel(ylabel)
        if title is not None:
            plt.title(title)

        maxy = 0.01 # np.-1inf
        miny = -0.01 # np.inf

        try:
            plt.style.use("macro")
        except:
            pass

        plt.grid(False)
        # plot upper half

        colors = ["red","maroon","lightcoral","gold","crimson","orange"] # plot colors
        color_idx = 0
        last_vals = None

        for k,v in entries.items():

            for k2,v2 in v.items():

                if  k2 == BalanceEntry.ASSETS:
                    if len(v2) > 0:
                        idx = [int(i) for i in np.arange(0,len(v2)-1,dt)]
                        # idx2 = [str(Clock().get_i) for i in idx]
                        idx2 = [str(i) for i in idx]

                        #print("idx2",idx2)
                        vals = [v2[i] for i in idx]
                        # print("vals",vals)

                        maxy = max(maxy,np.max(vals))
                        miny = min(miny,np.min(vals))

                        plt.bar(idx2,vals,label=str(k),color=colors[color_idx],alpha=0.9,bottom=last_vals)

                        if last_vals is None:
                            last_vals = np.array(vals)
                        else:
                            last_vals += np.array(vals)

                        color_idx += 1
                        color_idx = color_idx % len(colors)


        colors = ["black","blue","navy","dodgerblue","royalblue","slateblue"] # plot colors
        color_idx = 0
        last_vals = None

        for k,v in entries.items():
            for k2,v2 in v.items():

                if  not k2 == BalanceEntry.ASSETS:

                    if len(v2) > 0:
                        idx = [int(i) for i in np.arange(0,len(v2)-1,dt)]
                        # idx2 = [str(Clock().get_i) for i in idx]
                        idx2 = [str(i) for i in idx]

                        #print("idx2",idx2)
                        vals = [v2[i] for i in idx]
                        # print("vals",vals)

                        maxy = max(maxy,np.max(vals))
                        miny = min(miny,np.min(vals))

                        plt.bar(idx2,vals,label=str(k),color=colors[color_idx],alpha=0.9,bottom=last_vals)

                        if last_vals is None:
                            last_vals = np.array(vals)
                        else:
                            last_vals += np.array(vals)

                        color_idx += 1
                        color_idx = color_idx % len(colors)

        # downward ticks
        # https://stackoverflow.com/questions/50571287/how-to-create-upside-down-bar-graphs-with-shared-x-axis-with-matplotlib-seabor

        plt.xticks(rotation=90)

        #if show_liabilities:
        #    plt.ylim([1.3*miny,1.8*maxy+ .2*max(0,len(entries.keys())-3)])
        #else:
        #    plt.ylim([1.3*miny,1.4*maxy+ .2*max(0,len(entries.keys())-3)])


        ticks =  plt.gca().get_yticks()
        myticks_abs = [(abs(tick)) for tick in ticks]
        myticks = [((tick)) for tick in ticks]
        plt.gca().set_yticks(myticks)
        plt.gca().set_yticklabels(myticks_abs)

        plt.legend(loc=(1.04,0)) # "upper left")

        plt.tight_layout()
        if show:
            plt.show()

        return plt.gcf()
