# Deme Kristóf
# Stat 2. (GY) 9. házi feladat

# szükséges modulok
import pandas
import numpy
import recode # requires same directory
from scipy.stats import ttest_1samp

# a .sav fájlt áttettem egy .xlsx-be, ebből az adatból dolgozik a kód
dataset = pandas.read_excel('dataset.xlsx', header=0, index_col=1, dtype=str)

# Numpy array listákkal szedtem ki a fontos két változómat
paeduc = numpy.array(dataset["Highest Year School Completed, Father"],dtype=str)
educ = numpy.array(dataset["Highest Year of School Completed"],dtype=str)

# a recode miatt sima python listákra váltok (rosszabb performancia, de könnyebb kezelhetőség), a string-eket viszem integerbe a recode során
respondent_edu = []
father_edu = []
respondent_categ = []
father_categ = []

recode.recode_values(paeduc,father_edu)
recode.recode_values(educ,respondent_edu)
recode.categorize(respondent_edu,respondent_categ)
recode.categorize(father_edu,father_categ)

# DataFrame konstruktor
data_frame = pandas.DataFrame({"Highest Year of School Completed": respondent_edu,
                                "Highest Year School Completed, Father": father_edu,
                               "Highest Year of School Completed in categories":respondent_categ,
                               "Highest Year School Completed, Father in categories":father_categ})

# adattisztítás 97,98,99 & üres elemekre, amik -1 értéket vesznek fel
data_frame = data_frame.loc[(data_frame["Highest Year of School Completed"] != -1) & (data_frame["Highest Year School Completed, Father"] != -1)]

# a két diszkrét változó különbségeinek átlaga
mean_diff = numpy.mean(data_frame["Highest Year of School Completed"]-data_frame["Highest Year School Completed, Father"])

# 'tesztstatisztika'
t_statistic_1, p_value1 = ttest_1samp(data_frame["Highest Year of School Completed"]-data_frame["Highest Year School Completed, Father"],0)
print(t_statistic_1, ' ', p_value1)

# döntés a hipotéziseinkről
def decision_1():
    print('P value is:',p_value1)
    if p_value1 < 0.05:
        print("There is evidence at the chosen significance level that the respondents are more educated than their fathers.")
    else:
        print("There is no evidence at the chosen significance level that the respondents are more educated than their fathers.")
decision_1()
def mean_respondent():
    # megkérdezettek átlaga
    mean_resp = data_frame["Highest Year of School Completed"].mean()

    print("Mean of column 'Highest Year of School Completed':", mean_resp)
mean_respondent()
def mean_father():
    # apjuk átlaga
    mean_fath = data_frame["Highest Year School Completed, Father"].mean()

    print("Mean of column 'Highest Year School Completed, Father':", mean_fath)
mean_father()
def std_dev_respondent():
    # megkérdezettek szórása
    std_dev_resp = data_frame["Highest Year of School Completed"].std()

    print("Standard deviation of column 'Highest Year of School Completed':", std_dev_resp)
std_dev_respondent()
def std_dev_respondent():
    # apjuk szórása
    std_dev_fath = data_frame["Highest Year School Completed, Father"].std()

    print("Standard deviation of column 'Highest Year School Completed, Father':", std_dev_fath)
std_dev_respondent()

crosstable = pandas.crosstab(data_frame["Highest Year of School Completed in categories"],data_frame["Highest Year School Completed, Father in categories"], margins=True)
crosstable = crosstable.rename(index={1:'Primary',2:'Secondary',3:'Higher'},columns={1:'Primary',2:'Secondary',3:'Higher'})
print(crosstable)