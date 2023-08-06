import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import t
from scipy.stats import f
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
import numpy as np
from scipy import stats
import statsmodels.stats.diagnostic as dg
from scipy.stats import shapiro
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
class regression:
  def __init__(self, df_y, df_x):
    self.n = df_x.shape[0]
    try:
      self.k = df_x.shape[1]
    except:
      self.k = 1
    self.df_x = df_x
    self.df_y = df_y
    self.df_x_b = sm.add_constant(df_x)
    self.model = sm.OLS(self.df_y,self.df_x_b).fit()
    self.rnd_dev = self.model.predict(self.df_x_b) - np.array(self.df_y)

  def func(self):
    print("""
    print(.__doc__)
    params()
    significance_of_parameters(0.05)
    fisher(0.05)
    betta(self)
    delta(self)
    elastic(self)
    predict(pd.DataFrame([[1,1,2],[1,2,2]], columns = ['const','x1','x2']), 'x1')
    breuschpagan()
    Goldfeld_Qandt()
    spearmen(col)
    park(col)
    glayzer(col)
    white(col)
    dw()
    series_method(0.05)
    reset()
    shapiro_wilka()
    jarque_bera()
    VIF()""")


  def params(self):
    return self.model.params

  def significance_of_parameters(self, a):
    """|t_calc| < t_tabl not significant"""
    print('t_tabl:', t.ppf(1-a, self.n-self.k-1))
    print('t_calc:\n', self.model.tvalues)
    

  def fisher(self, a):
    """Н0: b_1 = ... = b_n = 0
Н1: b_1 != ... != b_n != 0

If F_calc > F_tabl, then Н0 rejected"""
    print('F_tabl:', f.ppf(1-a,self.k, self.n-self.k-1))
    print('F_calc:', self.model.fvalue)
    
  def R(self):
    print('R = ',self.model.rsquared)
    print('R_adj = ',self.model.rsquared_adj)
    print('Average relative approximation errors = ', sum(abs(((self.model.predict(self.df_x_b)-self.df_y)/self.df_y)))/(self.n))

  def predict(self, X, col):
    """pd.DataFrame([[1,1,2],[1,2,2]], columns = ['const','x1','x2']), 'x1' """
    P = self.model.predict(X)
    print('y = ', P)
  
    Se_2 = 1/(self.n-self.k-1)*sum((self.df_y - self.df_y.mean())**2)
    Se = Se_2**0.5      
    X = X[col]
    min_ = P-Se * t.ppf(1-0.05, self.n-self.k-1) * (1 + 1/self.n + (X-self.df_x.mean())**2/(sum((self.df_x-self.df_x.mean()**2))) )**0.5
    max_ = P[0]+Se * t.ppf(1-0.05, self.n-self.k-1) * (1 + 1/self.n + (X-self.df_x.mean())**2/(sum((self.df_x-self.df_x.mean()**2))) )**0.5
    print('Confidence interval Y:\n from', min_, '\n to', max_)

  def breuschpagan(self):
    """If p_value > a homoscedasticity"""
    names = ['Lagrange multiplier statistic', 'p-value','f-value', 'f p-value']
    test = sms.het_breuschpagan(self.model.resid, self.model.model.exog)
    print(lzip(names, test)[1])
  
  def Goldfeld_Qandt(self):
    """If p_value > a homoscedasticity"""
    test = sm.stats.diagnostic.het_goldfeldquandt(self.df_y, self.df_x_b, drop=0.2)
    print('p_value -', test[1])

  def spearmen(self, col):
    """if p_value > a homoscedasticity"""
    test = stats.spearmanr(self.df_x[col], abs(np.array(self.rnd_dev)))
    print(test)
  
  def park(self, col):
    """if coeff significance not homoscedasticity
      P < a"""
    import pandas as pd
    x = np.array(self.df_x[col])
    ln_x = np.log(x)
    u_2 = np.array(self.rnd_dev)**2
    ln_u_2 = np.log(u_2)

    X = pd.DataFrame({'ln(x)':ln_x})
    X = sm.add_constant(X)

    model = sm.OLS(ln_u_2, X)
    results = model.fit()
    print(results.summary().tables[1])

  def glayzer(self, col):
    """if coeff significance not homoscedasticity
      P < a"""
    x = np.array(self.df_x[col])
    u = abs(np.array(self.rnd_dev))

    # x**(-1)
    X = 1/x
    X = sm.add_constant(X)
    model = sm.OLS(u, X)
    results = model.fit()
    print(results.summary().tables[1])

    # x**(-0.5)
    X = 1/x**(0.5)
    X = sm.add_constant(X)
    model = sm.OLS(u, X)
    results = model.fit()
    print(results.summary().tables[1])

    # x**(0.5)
    X = x**(0.5)
    X = sm.add_constant(X)
    model = sm.OLS(u, X)
    results = model.fit()
    print(results.summary().tables[1])

    # x**(-1)
    X = x**(1.5)
    X = sm.add_constant(X)
    model = sm.OLS(u, X)
    results = model.fit()
    print(results.summary().tables[1])

    # x
    X = x
    X = sm.add_constant(X)
    model = sm.OLS(u, X)
    results = model.fit()
    print(results.summary().tables[1])


  def white(self, col):
    """if coeff significance not homoscedasticity
      P < a"""
    import pandas as pd
    x = np.array(self.df_x[col])
    x_2 = np.array(self.df_x[col])**2
    u_2 = np.array(self.rnd_dev)**2

    X = pd.DataFrame({'x':x,'x_2':x_2})
    X = sm.add_constant(X)

    model = sm.OLS(u_2, X)
    results = model.fit()
    print(results.summary().tables[1])

  def dw(self):
    import pandas as pd
    Durbin_Wotson = pd.DataFrame(self.model.summary().tables[2])[3].loc[0]
    Durbin_Wotson = float(str(Durbin_Wotson).replace(' ',''))
    dl = 1.27
    du = 1.45

    a = 0
    b = 4
    print('Durbin_Wotson=', Durbin_Wotson)
    print(f'{a:0.2f}---{dl:0.2f}---{du:0.2f}---{(b-du):0.2f}---{(b-dl):0.2f}---{b:0.2f}')
    print('    cov>0        cov=0         cov<0')

  def series_method(self, a):
    """if <k< not autocorrelation"""
    sp = self.rnd_dev
    n1 = len(sp[sp>0])
    n2 = len(sp[sp<0])
    
    k = 1
    for ind in range(1, len(sp)):
      if (sp[ind-1] > 0 and sp[ind] < 0) or (sp[ind-1] < 0 and sp[ind] > 0):
        k+=1

    E = 2*n1*n2/(n1+n2)
    D = (2*n1*n2*(2*n1*n2-n1-n2))/((n1+n2)**2)*(n1+n2-1)
    u = stats.norm.ppf(1 - a/2)
    print('left -', E-u*D)
    print('k -', k)
    print('right -', E+u*D)

  def reset(self):
    """p_value > 0.05 No new"""

    reset = dg.linear_reset(self.model, power = 2, test_type = 'fitted', use_f = True)
    print('Ramsey-Reset Test F-Statistics:', np.round(reset.fvalue, 6))
    print('Ramsey-Reset Test P-Value:', np.round(reset.pvalue, 6))
    
  def shapiro_wilka(self):
    """if p_value > a norm"""
    print('p_value', shapiro(self.rnd_dev)[1])

  def jarque_bera(self):
    """if p_value > a norm"""
    print('p_value', stats.jarque_bera(self.rnd_dev)[1])

  def betta(self):
    for el in self.df_x.columns:
      
      print('betta',el,'-',self.model.params[el]*(np.var(self.df_x[el], ddof = 1))**0.5/(np.var(self.df_y, ddof = 1))**0.5)

  def delta(self):
    for el in self.df_x.columns:
      
      print('delta',el,'-',self.model.params[el]*np.mean(self.df_x[el])/(np.mean(self.df_y)))

  def elastic(self):
    matrix = self.df_x.join(self.df_y)
    for el in self.df_x.columns:
      r = matrix.corr().loc[['y'],[el]].values[0][0]

      print('elastic',el,'-',self.model.params[el]*r/self.model.rsquared)
      
  def VIF(self):
    import pandas as pd
    vif = pd.DataFrame()
    vif['VIF'] = [variance_inflation_factor(self.df_x.values, i) for i in range(self.df_x.shape[1])]
    vif['variable'] = self.df_x.columns
    print(vif)