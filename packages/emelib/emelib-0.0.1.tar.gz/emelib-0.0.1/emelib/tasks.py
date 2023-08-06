import json
import os
from typing import Dict, Any
from typing import Union
from typing import Optional
import string

import pathlib
from IPython.display import display, Markdown


class Task:
    class Fields:
        ID = "id"
        UNIT = "unit"
        TASK_TEXT = "task_text"
        TASK_SOLUTION_CODE_ANALYTICS = "task_solution_code_analytics"
        TASK_SOLUTION_CODE = "task_solution_code"

    def __init__(self, id: int = 0, unit: str = "test", task_text: str = "нет", task_solution_code_analytics: str = "нет", task_solution_code: str = "нет"):
        self.id = id
        self.unit = unit
        self.task_text = task_text
        self.task_solution_code_analytics = task_solution_code_analytics
        self.task_solution_code = task_solution_code

    @staticmethod
    def deserialize(data: Dict[str, Any]) -> 'Task':
        return Task(
            id=data.get(Task.Fields.ID),
            unit=data.get(Task.Fields.UNIT),
            task_text=data.get(Task.Fields.TASK_TEXT),
            task_solution_code_analytics=data.get(Task.Fields.TASK_SOLUTION_CODE_ANALYTICS),
            task_solution_code=data.get(Task.Fields.TASK_SOLUTION_CODE)
        )

def help():
    print('1. emelib.find_by_words("любое количество слов"), unit="q3"')
    print('unit можно не писать, опции: test, q3, q2, q1')
    print('2. task = emelib.get_task_by_id(выбранный_id)')
    print('3. print(task.task_solution_code_analytics)')
    print('4. если там теор -- выполните команду, иначе ctrl c ctrl v, не забудьте поменять цифры')
    print('если все плохо -- emelib.load_all_unit_tasks("test"|"q3"|"q2"|"q1")')

def load_all_tasks():
    all_tasks = []
    with open(pathlib.Path(pathlib.Path(os.path.dirname(os.path.abspath(__file__)), "tasks_base.txt")), encoding="UTF8") as f:
        for row in f:
            all_tasks.append(Task.deserialize(json.loads(row)))
    return all_tasks


def get_task_by_id(id: int) -> Union['Task', str]:
    all_tasks = load_all_tasks()
    for task in all_tasks:
        if task.id == id:
            return task
    return "NO TASK WITH THAT WORD, CHECK IT"


def find_by_words(words: str, unit: Optional[str] = None):
    words = words.split()
    words = [w.lower().replace("ё","е") for w in words]
    all_tasks = load_all_tasks()
    counter = [0 for _ in range(max([task.id for task in all_tasks]) + 4)]
    for task in all_tasks:
        task_words = task.task_text.translate(str.maketrans('', '', string.punctuation))
        task_words = task_words.split(" ")
        task_words = [w.lower().replace("ё", "е") for w in task_words]
        for word in words:
            if word in task_words:
                counter[task.id] += 1
    all_tasks_by_id = {task.id: task for task in all_tasks}
    c = [[counter[i], i] for i in range(len(counter))]
    c.sort(reverse=True)
    for el in c:
        if el[0] > 0:
            i = el[1]
            task = all_tasks_by_id[i]
            text = task.task_text
            if unit:
                if task.unit == unit:
                    print(i, "\n".join([text[128 * i:128 * (i + 1)] for i in range(0, (len(text) - 1) // 128 + 1)]))
            else:
                print(i, "\n".join([text[128*i:128*(i + 1)] for i in range(0, (len(text) - 1) // 128 + 1)]))


def load_all_unit_tasks(unit: str):
    all_tasks = load_all_tasks()
    for task in all_tasks:
        if task.unit == unit:
            print(task.id, task.task_text)


def sample_and_sample_choice_function():
    display(Markdown(r"""
    $ n\hat{F(x)}  \sim Bin(n, F(x)); F(x) = \frac{x-a}{b-a} $  

$ a)P((\hat{F(6)}=\hat{F(8)}) = P(X_i  \nsubseteq [5,8]) = (1-\frac{2}{3})^6 \approx 0,0014$  

$ б) Y = 6\hat{F(7)}\sim Bin(6, \frac{2}{3})  $  
$ P(\hat{F(7)})=\frac{1}{2} = P(Y=3) = С^3_6 p^3 (1-p)^3 = \frac{4 \cdot 5 \cdot 6}{6} \cdot (\frac{2}{3})^3 \cdot (\frac{1}{3})^3  \approx 0,2195$  
    """))


def sample_and_gen_function():
    display(Markdown(r"""
$ X_1,..., X_n$ - выборка 

$ X_i  \thicksim L_\theta(X)$ 

$L_\theta(x)$ имеет функцию распределния $F(x)$

$ X_{(1)},.., X_{(n)} $ - вариационный ряд

$ X_{(1)}\leq..\leq X_{(n)} \Rightarrow X_{(1)} = \min(X_1,.., X_n); X_{(n)}=\max(X_1,.., X_n) $

$ 1) F_{X_{(n)}} = P(X_{(n)} < x) = P(\max(X_1,.., X_n)<x) = P(X_1<x) \cdot...\cdot P(X_n<x)= F(x)\cdot...\cdot F(x) = (F(x))^n   $

$ 2) F_{X_{(1)}} = P(X_{(1)} < x) = P(\min(X_1,.., X_n)<x) = 1 - P(\min(X_1,.., X_n) > x)= 1 - P(X_1>x) \cdot...\cdot P(X_n>x) = 1 - \prod^n_{k=1}[1-P(X_k <x)] = 1 - \prod^n_{k=1}[1- F(x)] = 1-(1-F(x))^n $


  """))

def unmoved_marks():
    display(Markdown(r"""
а) $E(X^2) = \{Var(X) = E(X^2) - [E(X)]^2 \} = Var(X) + [E(X)]^2 = \sigma^2 + \theta^2 \neq \theta^2  \Rightarrow$ не явлется несмещенной  
б) $E(Z) = E(X \cdot Y) = E(X) \cdot E(Y) = \theta \cdot \theta = \theta^2  \Rightarrow несмещенная $
      """))


def prove_std():
    display(Markdown(r"""
$ E[(\hat{\theta} − \theta)^2] = E[(\hat{\theta})^2 - 2 \cdot \theta \cdot \hat{\theta} + \theta^2] = E((\hat{\theta})^2) - 2 \cdot \theta \cdot E(\hat{\theta}) + \theta^2 = \{Var(\hat{\theta}) = E((\hat{\theta})^2) - [E(\hat{\theta})]^2 \} = Var(\hat{\theta}) + [E(\hat{\theta})]^2 -  2 \cdot \theta \cdot E(\hat{\theta}) + \theta^2 = Var(\hat{\theta}) + (E[\hat{\theta}] - \theta))^2 = Var(\hat{\theta}) + b^2$ 
      """))


def best_std():
    display(Markdown(r"""
    $ 1) E(\hat{\theta}) = E(aX_1+2aX_2) = aE(X_1) + 2aE(X_2) = a\theta + 2a\theta = 3a\theta$  
$ Var(\hat{\theta}) = Var(aX_1+2aX_2) = a^2Var(X_1) + 4a^2Var(X_2) = 5a^2\sigma^2 = a^2\frac{3 \cdot 5}{5}\theta^2 = 3a^2\theta^2 $  
$ 2) ∆ = Var(\hat{\theta}) + b^2 $  
$b = (E[\hat{\theta}] − \theta) = E(aX_1+2aX_2) - \theta = 3a\theta - \theta = \theta(3a-1)$  
$ ∆ = Var(\hat{\theta}) + (\theta(3a-1))^2 = 3a^2\theta^2  + \theta^2(3a-1)^2 = \theta^2(12a^2-6a+1) $  
$ f = (12a^2-6a+1)$  
$ f\prime = 24a-6 = 0$  
$ a= \frac{1}{4}  \Rightarrow \hat{\theta} =  \frac{X_1}{4} +  \frac{X_2}{2}$  
Проверим на несмещенность  
$ E(\hat{\theta}) = E(\frac{X_1}{4} +  \frac{X_2}{2}) = \frac{1}{4}E(X_1) + \frac{1}{2}E(X_2)=\frac{3}{4}\theta \neq \theta$  
Не является несмещенной 

    """))

# todo: 6b
def prove_random_facts():
    display(Markdown(r"""
$a)\mu_3(\bar{X}) = \mu_3(\frac{X_1+...+X_n}{n}) = \{\mu_3(\frac{X_i}{n}) = E([\frac{X_i}{n}-E(\frac{X_i}{n})]^3) = E(\frac{1}{n^3}[X_i - E(X_i)]^3) = \frac{1}{n^3}\mu_3(X_i)\} = \frac{1}{n^3}[\mu_3(X_1)+...+\mu_3(X_n)] = \frac{1}{n^3} \cdot n \mu_3(X) = \frac{\mu_3(X)}{n^2}  $  

$б) \mu_4(\bar{X}) = $

         """))

def gen_dist_unmoved():
    display(Markdown(r"""
$ a) \hat{\theta}_1 = c_1(X_1 - X_2)^2 $  
$ E(\hat{\theta}_1) = E(c_1(X_1 - X_2)^2) = c_1E(X_1^2)-2c_1E(X_1\cdot X_2) +c_1E(X_2^2) = \{ E(X_1^2) = Var(X_1) + [E(X_1)]^2 = \theta + \mu^2 \} = c_1(\theta + \mu^2) - 2c_1E(X_1)E(X_2) + c_1(\theta + \mu^2) = 2c_1(\theta + \mu^2) -2c_1\mu^2 = 2c_1\theta \Rightarrow c_1 = \frac{1}{2}    $


$ б) \hat{\theta}_2 = c_2[(X_1 - X_2)^2 + (X_1 - X_3)^2 + (X_2 - X_3)^2] $

$ E(\hat{\theta}_2) = c_2(E[(X_1 - X_2)^2] + E[(X_1 - X_3)^2] + E[(X_2 - X_3)^2]) $

$ E((X_1-X_2)^2) = E(X_1^2)-2E(X_1\cdot X_2) +E(X_2^2) = 2\theta $ пункт a  

$ E(\hat{\theta}_2) = c_2(2\theta + 2\theta +2\theta) = 6c_2\theta \Rightarrow c_2 = \frac{1}{6} $
         """))


def example_dist_unmoved():
    display(Markdown(r"""
$ a) 1) E(\hat{\theta}_1) = E(\frac{X1+2X2+3X3+4X4}{10}) = \frac{1}{10}[E(X_1) + 2E(X_2) + 3E(X_3) + 4E(X_4)] = \theta10 \cdot \frac{1}{10} = \theta \Rightarrow $ несмещанная  
$ 2) E(\hat{\theta}_2) = E(\frac{X1+4X2+4X3+X4}{10}) = \frac{1}{10}[E(X_1) + 4E(X_2) + 4E(X_3) + 1E(X_4)] = \theta10 \cdot \frac{1}{10} = \theta \Rightarrow $ несмещанная  
Оптимальная та, у который  $ б) min(Var(X_i))$  
$ 1) Var((\hat{\theta}_1) = Var(\frac{X1+2X2+3X3+4X4}{10}) = \frac{1}{100}[Var(X_1) + 4Var(X_2) + 9Var(X_3) + 16Var(X_4)] = \theta30 \cdot \frac{1}{100} = \frac{3}{10}\theta $  
$ 2) Var((\hat{\theta}_2) = Var(\frac{X1+4X2+4X3+1X4}{10}) = \frac{1}{100}[Var(X_1) + 16Var(X_2) + 16Var(X_3) + 1Var(X_4)] = \theta36 \cdot \frac{1}{100} = \frac{36}{100}\theta$  
$ \frac{3}{10} < \frac{36}{100} \Rightarrow \hat{\theta}_1$ оптимальнее  

         """))


def gen_dist_tetta():
    display(Markdown(r"""
$ a) 1) E(\hat{\theta}_1) = E(\frac{X_1+X_2}{2}) = \frac{1}{2}[E(X_1)+E(X_2)]= \frac{1}{2}\cdot2\theta = \theta  \Rightarrow $ несмещанная  
$ 2) E(\hat{\theta}_2) = E(\frac{X_1+X_n}{4} + \frac{X_2+...+X_(n-1)}{2(n-2)}) = \frac{1}{4}[E(X_1)+E(X_n)] + \frac{1}{2(n-2)}[E(X_2)+...+E(X_(n-1)] = \frac{2}{4}\theta + \frac{(n-2)}{2(n-2)}\theta = \theta \Rightarrow $ несмещанная  
$ 3) E(\hat{\theta}_3) = E(\bar{X}) = E( \frac{X_1+...+X_n}{n}) = \frac{1}{n}[E(X_1)+..+E(X_n)] = \frac{1}{n} \cdot n\theta = \theta \Rightarrow $ несмещанная  


$ б) 1) Var(\hat{\theta}_1) = Var(\frac{X_1+X_2}{2}) = \frac{1}{4}[Var(X_1)+Var(X_2)]= \frac{1}{4}\cdot2\sigma^2 = \frac{1}{2}\sigma^2; \lim\limits_{n\to\infty}(\frac{1}{2}\sigma^2)\neq 0\Rightarrow $ несостоятельная  
$ 2) Var(\hat{\theta}_2) = Var(\frac{X_1+X_n}{4} + \frac{X_2+...+X_(n-1)}{2(n-2)}) = \frac{1}{16}[Var(X_1)+Var(X_n)] + \frac{1}{4(n-2)^2}[Var(X_2)+...+Var (X_(n-1)] =  \frac{1}{8}\sigma^2 + \frac{1}{4(n-2)}\sigma^2 ; \lim\limits_{n\to\infty}(\frac{1}{8}\sigma^2 + \frac{1}{4(n-2)}\sigma^2 )\neq 0\Rightarrow $ несостоятельная  
$ 3) Var(\hat{\theta}_3) = Var(\bar{X})= \frac{1}{n^2}[Var(X_1) +...+Var(X_n)] = \frac{1}{n^2} \cdot n\sigma^2 = \frac{1}{n}\sigma^2; \lim\limits_{n\to\infty}(\frac{1}{n}\sigma^2 = 0\Rightarrow $ состоятельная 
         """))


def uniform_dist_tetta():
    display(Markdown(r"""
$ F_x(x) = \frac{x}{\theta}$

$ f_x(x) = \frac{1}{\theta}$

$ E(X) = \frac{\theta}{2}$

$ Var(X) = \frac{\theta^2}{12}$


$ \hat{\theta}_1 = 2\bar{X}$

$ E(\hat{\theta}_1) = E(2\bar{X}) = 2E(\frac{X_1+...+X_2}{n}) = \frac{2}{n}E(X_1+..+X_2) =\frac{2}{n}E(X_i) = \frac{2}{n} \cdot n \cdot \frac{\theta}{2} = \theta \Rightarrow $ несмещенная


$ Var(\hat{\theta}_1) = Var(2\bar{X}) = 4[Var(\frac{X_1+...+X_n}{n})] = 4 \cdot \frac{1}{n} \cdot Var(X_i) = \frac{4 \cdot \theta^2}{n \cdot 12} = \frac{ \theta^2}{n \cdot 3}; \lim\limits_{n\to\infty}(\frac{ \theta^2}{n \cdot 3}) = 0\Rightarrow $ состоятельная  


$ \hat{\theta}_2 = \frac{n+1}{n}X_{(n)} $  

$ F_{x_{(n)}}(x) = F_{X_{(n)}} = P(X_{(n)} < x) = P(\max(X_1,.., X_n)<x) = P(X_1<x) \cdot...\cdot P(X_n<x)= F(x)\cdot...\cdot F(x) = (F(x))^n = (\frac{x}{\theta})^n  $

$ f_{x_{(n)}}(x) = ((F(x))^n)' = nF^{n-1}(x) = n * \frac{x^{n-1}}{\theta^n} $



$ E(\hat{\theta}_2) = E(\frac{n+1}{n}X_{(n)}) = \frac{n+1}{n} \cdot \int_{0}^\theta x * n * \frac{x^{n-1}}{\theta^n} dx = \frac{n+1}{n} * \frac{n}{\theta^n} \int_{0}^\theta x^n dx  = \theta \Rightarrow $ несмещенная


         """))


def uniform_tetta_another_version():
    display(Markdown(r"""
$ F_x(x) = \frac{x}{\theta}$

$ f_x(x) = \frac{1}{\theta}$

$ E(X) = \frac{\theta}{2}$

$ Var(X) = \frac{\theta^2}{12}$


$ \hat{\theta}_1 = 2\bar{X}$

$ E(\hat{\theta}_1) = E(2\bar{X}) = 2E(\frac{X_1+...+X_2}{n}) = \frac{2}{n}E(X_1+..+X_2) =\frac{2}{n}E(X_i) = \frac{2}{n} \cdot n \cdot \frac{\theta}{2} = \theta  \Rightarrow $ несмещенная

$ Var(\hat{\theta}_1) = Var(2\bar{X}) = 4[Var(\frac{X_1+...+X_n}{n})] = 4 \cdot \frac{1}{n} \cdot Var(X_i) = \frac{4 \cdot \theta^2}{n \cdot 12} = \frac{ \theta^2}{n \cdot 3}; \lim\limits_{n\to\infty}(\frac{ \theta^2}{n \cdot 3}) = 0\Rightarrow $ состоятельная  

$X_{1}, ... X_{n} \sim  \mathcal{U} ([0; \theta])$   

$\theta$ > 0
 
a) $\theta = 2\overline{X}$

$\mathbb{E}(\widehat{\theta}_{1}) = \theta = \mathbb{E}(2\overline{X}) = 2 \mathbb{E}(X)= 2 *\frac{\theta}{2} = \theta$

$\forall \theta > 0$

=> $\widehat{\theta}_{1}$- несмещенная

б) Var($\widehat{\theta}_{1}$ = Var(2$\overline{X}$) = 4Var($\overline{X}$) = 4$\frac{\sigma^{2}}{n}$ = 4 * $\frac{\sigma^{2}}{12} * \frac{1}{n} -> 0$

$n -> \infty$

$\widehat{\theta}_{1}$ - сост
______________________________________

$\widehat{\theta}_{2} = (n+1) * X_{(1)}$

$\mathbb{E}(\widehat{\theta}_{2}) = (n+1) \mathbb{E}(X_{(1)})$

$X_{(1)} = min(X_{1}, ..., X_{n})$ = 
=$F_{X_{(1)}}(x) =\mathbb{P}(X_{(1)} \le x) = \mathbb{P}(min(X_{1}, ..., X_{n}) \le x) = 1 -  \mathbb{P}(X_{1} \ge x, ..., X_{n} \ge x) $

$1 - (1 - F_{x}(x))^{n}$

$= (\mathbb{P}(X_{i} \le x ))^{n} =$ $F_{X}^{n}(x)$= $(\frac{x}{\theta})^{n}$

$F_{X}(x) $=$\left\{ \begin{array}{rcl}
0 & \mbox{ }
& x \le  \theta \\ \frac{x-0}{\theta} & \mbox{ } & 0 \le x \le \theta \\
\end{array}\right.$

$f(x) = F_{X}^{'}(x) =n(1- F_{x}(x))^{n-1} * f_{x}(x)$ $ 0 \le x \le \theta$

=$ n (1- \frac{x}{\theta})^ {n-1} * \frac{1}{\theta}$

$\mathbb{E}(\widehat{\theta_{2}}) = (n+1) \mathbb{E}(X_{(1)}) = (n+1) \int_{0}^{\theta} x * n (1-\frac{x}{\theta})^{n-1} * \frac{1}{\theta}dx=\frac{(n+1)n}{\theta^{n-1} \theta}*\int_{0}^{\theta} x (\theta -x)^{n-1}dx$

$ \bigg | \begin{array}{rcl} t = \theta-x\\ x= \theta - t \\ dt = -dx\end{array} $

= - $\frac{(n+1)n}{\theta ^ {n}} (\int_{0}^{\theta} \theta t^{n-1}dt - \int_{0}^{\theta}  t^{n}dt) = \frac{(n+1)n}{\theta ^{n}} *(\theta * \frac{\theta^{n}}{n} - \frac{\theta^{n+1}}{n+1}) = \frac{(n+1)n}{\theta ^{n}} * \theta ^ {n+1} (\frac{1}{n} -  \frac{1}{n+1}) = \frac{(n+1)n \theta ^{n+1}} {\theta^{n}} (\frac{1}{n(n+1)}) = \theta 
\forall $
 """))


def rand_value_3():
    display(Markdown(r"""
$ E(X_i) = \frac{0+\theta}{2} = \frac{\theta}{2}; Var(X_i) = \frac{(\theta-0)^2}{12}= \frac{\theta^2}{12}; f(x,\theta)= \frac{1}{\theta}; n=3 $  
$ \hat{\theta} = c \cdot \bar{X} = c \cdot \frac{X_1+X_2+X_3}{3}$  
$ a) E(\hat{\theta}) = E(c \cdot \frac{X_1+X_2+X_3}{3}) = \frac{c}{3}[E(X_1)+E(X_2)+E(X_3)] = \frac{3cE(X_i)}{3} = c \cdot \frac{\theta}{2} = \theta \Rightarrow c=2  $  
$ б) Var(\hat{\theta}) = \frac{1}{nI(\theta)}; I(\theta)= nE[(\frac{\partial lnf(x,\theta)}{\partial \theta})^2] $  
$ \ln(f(x,\theta)) = \ln(\frac{1}{\theta})= -\ln(\theta)$  
$ (\frac{\partial lnf(x,\theta)}{\partial \theta})^2 = (\frac{-1}{\theta})^2= \frac{1}{\theta^2}  $  
$ I(\theta)= nE[\frac{1}{\theta^2}] = \frac{n}{\theta^2} $  
$ Var(\hat{\theta}) = Var(c \cdot \frac{X_1+X_2+X_3}{3}) = \frac{c^2}{9}[Var(X_1)+Var(X_2)+Var(X_3)]= \frac{c^2}{9}Var(X_i)= \frac{c^2\theta^2}{36} $  
$ \frac{c^2\theta^2}{36} = \frac{1}{\frac{9}{\theta^2}} \Rightarrow \frac{c^2}{36} =\frac{1}{9} \Rightarrow c =2  $
         """))


def sqrt_param_tetta():
    display(Markdown(r"""
$ a) E(\hat{\theta}) = E[\frac{3}{n}((X_1)^2+(X_2)^2+(X_3)^2))]= 3 \cdot \frac{3}{n}E[(X_i)^2] = 3 (Var(X_i) + [E(X_I)]^2) = 3( \frac{(b-a)^2}{12} + \frac{a+b}{2}) = 3(\frac{(\theta - (-\theta))^2}{12} = \frac{3\cdot4\theta^2}{12}= \theta^2 \Rightarrow $ несмещенная  
$ б) E(\sqrt{\hat{\theta}}) = E[\sqrt{\frac{3}{n}((X_1)^2+(X_2)^2+(X_3)^2)}) = E[\sqrt{3(X_i)^2}]= \sqrt{3}\left\lvert X_i \right\rvert = \sqrt{3} \int_{-\theta}^\theta \left\lvert X_i \right\rvert \cdot \frac{1}{2\theta} dX = \frac{\sqrt{3}}{2\theta}(-\int_{-\theta}^0 xdx + \int_{0}^\theta xdx) = \frac{\sqrt{3}}{2\theta} (\frac{\theta^2}{2}+ \frac{\theta^2}{2}) = \frac{\sqrt{3}}{2}\theta \Rightarrow $  
смещанная
         """))


def beta_eps_eq():
    display(Markdown(r"""
$$ \hat{\beta} =  \frac{\sum_{k=1}^{n}Y_k}{\sum_{k=1}^{n}x_i} = \frac{\sum_{k=1}^{n}\beta x_k + \epsilon_k}{\sum_{k=1}^{n}x_i} = \frac{\beta\sum_{k=1}^{n} x_k + \sum_{k=1}^{n}\epsilon_k}{\sum_{k=1}^{n}x_i}  = \beta + \frac{\sum_{k=1}^{n}\epsilon_k}{\sum_{k=1}^{n}x_i} $$
$ E(\hat{\beta}) = E(\beta + \frac{\sum_{k=1}^{n}\epsilon_k}{\sum_{k=1}^{n}x_i}) = \beta + E[\sum_{k=1}^{n}\epsilon_k] \cdot \frac{1}{\sum_{k=1}^{n}x_i} = \beta + n \cdot 0 \cdot \frac{1}{\sum_{k=1}^{n}x_i} = \beta  $
         """))


def beta_eps_another_version():
    display(Markdown(r"""
$ E(\hat{\beta}) = E[\frac{1}{n}\sum_{k=1}^{n}(\frac{Y_k}{x_k})] = \frac{1}{n}E[\sum_{k=1}^{n}(\frac{\beta x_k + \epsilon_k}{x_k})] = \frac{1}{n}E[\sum_{k=1}^{n}(\beta  + \frac{\epsilon_k}{x_k})] = \frac{1}{n}[E(\sum_{k=1}^{n}\frac{\epsilon_k}{x_k}) + \sum_{k=1}^{n}\beta] = \frac{1}{n}[n\cdot \beta + E(\frac{\epsilon_1}{x_1}+...+E(\frac{\epsilon_k}{x_k}=\frac{1}{n}(n\cdot \beta + \frac{0}{x_1} + \frac{0}{x_k}) = \beta   $
         """))


def poisson_moment():
    display(Markdown(r"""
$ a) \nu_1 = \hat{\nu_1}$ 

$\nu_1 = E(x) = \theta$

$\hat{\nu_1} = \bar{X} = \frac{0*146+1*97+..+10*2}{400}= 1,5375 = \hat{\theta}=\hat{\lambda} $


$ P(X>3) = 1 - P(X<3) = 1 - P(X=0) - P(X=1) - P(X=2) $

$ P(X=k)= \frac{\lambda^k\cdot \exp^{-\lambda}}{k!} $


$ P(X=0) = \frac{1,5375^0\cdot \exp^{-1,5375}}{0!} = 0,2149 $  
$ P(X=1) = \frac{1,5375^1\cdot \exp^{-1,5375}}{1!} = 0,3304 $  
$ P(X=2) = \frac{1,5375^2\cdot \exp^{-1,5375}}{2!} = 0,2540 $

$ P(X>3) = 1 - P(X<3) = 1 - P(X=0) - P(X=1) - P(X=2) = 1 - 0,2149 - 0,3304 - 0,2540 = 0,2007    $

$ б) P(X>3) = 1 - P(X<3) = 1 - (\frac{146+97+73}{400}) = 0.21 $

         """))


def moment_eval():
    display(Markdown(r"""
$V_1 = E(x) = \frac{(b-a)}{2} = \frac{(4\theta-0)}{2} = 2\theta $

$\hat{V_1}=\bar{X}  \Rightarrow 2\hat{\theta} = \bar{X} \Rightarrow \hat{\theta} = \frac{\bar{X}}{2}$

$ a) E(\hat{\theta}) = E(\frac{\bar{X}}{2}) = \frac{1}{2}E(\frac{X_1+...+X_n}{n}) = \frac{n}{2} \cdot nE(X_i) = \frac{1}{2} \cdot  2\theta = \theta \Rightarrow $ несмещенная


$Var(X_i) = \frac{(b-a)^2}{12}$

$ б) \lim\limits_{n\to\infty}(Var(\hat{\theta}) = \lim\limits_{n\to\infty}(Var(\frac{\bar{X}}{2}) = \lim\limits_{n\to\infty}\frac{1}{4}Var(\frac{X_1+..+X_n}{n}) = \lim\limits_{n\to\infty}\frac{1}{n^2 \cdot 4}Var(X_i) = \lim\limits_{n\to\infty}\frac{1(4\theta-0)^2}{n^2 \cdot 4} = \lim\limits_{n\to\infty}\frac{16\theta^2}{n^2 \cdot 4} = 0 \Rightarrow  $ состоятельная
         """))

def solve_some_dificult_number_18():
    display(Markdown(r"""
    $ X $ ~ $ U([a;b]) $

Найти методом моментов оценки для $a$ и $b$. 

Если для генерального распределения $\exists \nu_{2m}$, то $\hat{\varkappa_k}$ является состоятельной оценкой $\varkappa_k$, т.к. $\varkappa_k = f(\nu_1,...\nu_k)$, $\varkappa_k$ - многочлен степени $k$ и $\hat{\varkappa_k} = f(\hat{\nu_1},...\hat{\nu_k})$

$$
E(X) = \frac{a+b}{2}; Var(X) = \frac{(b-a)^2}{12}
$$


$$
\left\{
    \begin{array}\\
        \nu_1 = \frac{a+b}{2}\\
        \varkappa_2 = \frac{(b-a)^2}{12}
    \end{array}
\right. \Rightarrow \left\{
    \begin{array}\\
        \nu_1 = \frac{a+b}{2}\\
        \sqrt{3\varkappa_2} = \frac{b-a}{2}
    \end{array}
\right.
$$

$$
\left\{
    \begin{array}\\
        a = \nu_1 - \sqrt{3\varkappa_2}\\
        b = \nu_1 + \sqrt{3\varkappa_2}
    \end{array}
\right. \Rightarrow \text{метод моментов} \Rightarrow \left\{
    \begin{array}\\
        \hat{a}_{мм} = \hat{\nu_1} - \sqrt{3\hat{\varkappa_2}}\\
        \hat{b}_{мм} = \hat{\nu_1} + \sqrt{3\hat{\varkappa_2}}
    \end{array}
\right.
$$
    
           """))


def solve_some_dificult_number_19():
    display(Markdown(r"""
$X$ ~ Exp(λ); E(X) = $\frac{1}{λ}$ n = 200

| $x_i$  |  2,5 |  7,5 | 12,5  | 17,5  | 22,5  | 27,5  |
|---|---|---|---|---|---|---|
| $n_i$  | 133  |  45 |  13 |  6 | 2  |  1 |

Метод моментов: $\nu_k(\theta)=\hat{\nu_k}$

$$
\frac{1}{\hat{\lambda_{мм}}} = \nu_1; \hat{\lambda_{мм}} = \frac{1}{\hat{\nu_1}}=\frac{sum(n_i)}{2,5 \cdot 133 +...+27,5 \cdot 1} \approx 0,1980
$$

$$
F(x) = 1 - e^{-\lambda x} = 0,86
$$

$$
0,14 = e^{-\lambda x}
$$

$$
ln(0,14) = -\lambda x
$$

$$
x \approx 9,92986291
$$
           """))


def solve_some_dificult_number_20():
    display(Markdown(r"""
$ F(x) = x^{\beta}$, $x \in [0;1]$

Оценить методом моментов $\beta$

$f(x)=\beta x^{\beta - 1}$

$$
E(x) = \int_{0}^1 x\beta x^{\beta - 1}dx = \int_{0}^1 \beta x^{\beta}dx = \frac{{x^{\beta+1}}}{\beta+1} \bigg|_0^1 = \frac{\beta}{\beta+1}
$$

$\nu_1 = \frac{\beta}{\beta+1}$, $\hat{\nu_1} = 78\%$

$$
\frac{\hat{\beta}}{\hat{\beta}+1} = 0,78
$$

$\hat{\beta} = 3,54545454545$

$$
P(X<0,67)=0,67^{\hat{\beta}}=0,67^{3,54545454545}\approx 0,2417442353
$$
           """))


def solve_some_dificult_number_21():
    display(Markdown(r"""
Составим функцию правдоподобия:

$$
L(x, \lambda) = P_{\theta}(X=x_1)\cdot ...\cdot P_{\theta}(X=x_n) =
$$

$$
= \frac{\lambda^{x_1}}{x_1!}e^{-\lambda}\cdot...\cdot \frac{\lambda^{x_n}}{x_n!}e^{-\lambda} = \frac{\lambda^{n\bar x}}{x_1!\cdot...\cdot x_n!}e^{-\lambda n}
$$

Статистика $\hat{\theta}_n = \bar{\theta}_{ОМП}$ $(X_1,...,X_n)$ - оценка максимальной правдоподобности

$L(x,\bar{\theta}_{ОМП})= \sup_{\theta}L(X,\theta)\Rightarrow$

Если для $\forall$ реализации $x_1,...,x_n$ так $L(X;\theta)$ достигается во внутренней точке $\theta$ и $L(X,\theta)$ дифференц. по $\theta$, тогда $\bar{\theta}_{ОМП}$ удовлетвор.:

$$
\frac{d L(X,\theta)}{d \theta} = 0 \Leftrightarrow \frac{d lnL(X,\theta)}{d \theta} =0
$$

$$
lnL(X,\lambda)=n\bar{x}ln\lambda - lnx_1!\cdot ...\cdot x_n! - \lambda n
$$

$$
\frac{d lnL(X,\lambda)}{d \lambda} = \frac{n\bar{x}}{\lambda}-n
$$

$$
\lambda = \bar{x} \Rightarrow \text{макс., т. к } \frac{d^2lnL(X,\lambda)}{d^2\lambda} = \frac{-n\bar{x}}{\lambda^2} < 0 \Rightarrow \hat{\theta}_{ОМП}=\bar{x}
$$
           """))


def solve_some_dificult_number_22():
    display(Markdown(r"""
Составим функцию правдоподобия:

$$
L(x,\lambda)=f(x_1)\cdot...\cdot f(x_n)=\lambda^ne^{-\lambda n \bar{x}}
$$

Статистика $\hat{\theta}_n = \bar{\theta}_{ОМП}$ $(X_1,...,X_n)$ - оценка максимальной правдоподобности

$L(x,\bar{\theta}_{ОМП})= \sup_{\theta}L(X,\theta)\Rightarrow$

Если для $\forall$ реализации $x_1,...,x_n$ так $L(X;\theta)$ достигается во внутренней точке $\theta$ и $L(X,\theta)$ дифференц. по $\theta$, тогда $\bar{\theta}_{ОМП}$ удовлетвор.:

$$
\frac{d L(X,\theta)}{d \theta} = 0 \Leftrightarrow \frac{d lnL(X,\theta)}{d \theta} =0
$$

$$
lnL(X,\lambda)=ln\lambda^n\cdot e^{-\lambda n x} = ln\lambda^n-\lambda n \bar{x}
$$

$$
\frac{dln(X,\lambda)}{d\lambda}=\frac{n}{\lambda}-n\bar{x}
$$

$$
\frac{d^2lnL(X,\lambda)}{d^2\lambda} = \frac{-n}{\lambda^2} < 0 \text{ } \lambda = \frac{1}{\bar{x}} \Rightarrow
$$

$$
\hat{\theta}_{ОМП} = \frac{1}{\bar{x}}
$$
           """))


def solve_some_dificult_number_23():
    display(Markdown(r"""
$L(x,\theta) = \left\{
    \begin{array}\\
        \frac{1}{(b-a)^n}, a \leq \mathbb X_{(1)} \leq ... \leq \mathbb X_{(n)} \leq b\\
        0, \text{иначе}
    \end{array}
\right.$

$f_{U([a,b])} = \frac{1}{(b-a)} \Rightarrow$ Составим функцию max-правдоподобия:

$$
L(x,\theta) = \prod^n_{k=1}\frac{1}{b-a}=\frac{1}{(b-a)^n} \Rightarrow lnL(x,\theta)=ln\frac{1}{(b-a)^n}=-nln(b-a)
$$

$L(x,\theta) = \left\{
    \begin{array}\\
        \frac{dlnL(x,\theta)}{da}=\frac{n}{b-a}\\
        \frac{dlnL(x,\theta)}{db}=\frac{-n}{b-a}
    \end{array}
\right. \text{Система не имеет решений} \Rightarrow$

$\Rightarrow lnL(x,\theta_0) = \max_{\theta_0\in \theta}L(x,\theta)$

Построим график

$$
\hat{\theta}_{ОМП}=(1-\alpha)(\mathbb X_{(n)}-b+a)+\alpha \mathbb X_{(1)}, \alpha \in [0,1]
$$
           """))


def solve_some_dificult_number_24():
    display(Markdown(r"""
| X | -1       | 0           | 1         | 2         |
|---|----------|-------------|-----------|-----------|
| P | 𝜃 | 1-7𝜃 | 4𝜃 | 2𝜃 |

$\theta \in (0,\frac{1}{7})$

X = -1: $n_1$ раз.

X = 2: $n_4$ раз.

$n_1+n_2+n_3+n_4=n$

Составим функцию максимального правдоподобия:

$$
L(x,\theta) = (\theta)^{n_1}\cdot (4\theta)^{n_3} \cdot (2\theta)^{n_4} \cdot (1-7\theta)^{n_2} = \theta^{n_1+n_3+n_4}\cdot 2^{n_4+2n_3}\cdot (1-7\theta)^{n_2}
$$

$$
lnL(x,\theta)=(n_1+n_3+n_4)ln\theta + (2n_3+n_4)ln2 + n_2ln(1-7\theta)
$$

$$
\frac{dlnL(x,\theta)}{d\theta} = \frac{n_1+n_3+n_4 [=n-n_2]}{\theta}-\frac{7n_2}{1-7\theta}=0
$$

$$
\frac{n-n_2}{\theta}=\frac{7n_2}{1-7\theta}; \hat{\theta}=\frac{n-n_2}{7n}
$$

$E(\hat{\theta})=E(\frac{n-n_2}{7n})=\frac{1}{7n}[n-E(n_2)] = \begin{Bmatrix}
n_2 \sim Bin(n,p)\\
p = 1-7\theta\\
np=E(n_2)
\end{Bmatrix} = \frac{1}{7n}\cdot (n-n(1-7\theta)) = \frac{1-1+7\theta}{7}=\theta \Rightarrow \hat{\theta}_{ОМП} \text{ - несмещ.}$

$Var(\hat{\theta}) = Var(\frac{n-n_2}{7n}) = \frac{1}{49n^2}(Var(n)+Var(n_2)) = \frac{n(1-7\theta)7\theta}{49n^2} \rightarrow_{n\rightarrow \inf} 0 \Rightarrow \hat{\theta}_{ОМП} \text{ - самостоят.}$
           """))


def solve_some_dificult_number_25():
    display(Markdown(r"""
$X\sim C(x_0=\theta, \gamma=1)$

$X_1$ - единственное наблюдение $X$ имеет $f(x) = \frac{1}{\pi(1+(x-\theta)^2)}$

$$
\begin{matrix}
H_0: \theta = 0\\
H_1: \theta = 1
\end{matrix}
\begin{matrix}
\theta_0 = 0\\
\theta_1 = 1
\end{matrix}
\Rightarrow \frac{\frac{1}{\pi}\frac{1}{1+(x-1)^2}}{\frac{1}{\pi}\frac{1}{1+x^2}} = \frac{1+x^2}{x^2-2x+2}\geq c$$

Решим неравенство для нахождения критической области $c = 1$:

$$
T(\vec{x}) = \frac{1+x^2}{x^2-2x+2}\geq 1; \frac{-1+2x}{2+x^2-2x}\geq 0 \Rightarrow
$$

$$
x\geq \frac{1}{2} \text{ - критическая область}
$$

$$F(X)=\frac{1}{\pi}\arctan(x-\theta)+\frac{1}{2}$$

$$
\alpha = P_{H_0}(T(\vec{x}) \in k_{\alpha}) = P_{H_0}(x\geq \frac{1}{2}) = 1 - P_{H_0}(x< \frac{1}{2}) = \frac{1}{2}-\frac{1}{\pi}\arctan\frac{1}{2}
$$

$$
\beta = P_{H_0}(T(\vec{x})\notin k_{\alpha}) = P_{H_0}(x<\frac{1}{2})=\frac{1}{2}-\frac{1}{\pi}\arctan\frac{1}{2}
$$
           """))


def solve_some_dificult_number_26():
    display(Markdown(r"""
$X\sim C(x_0=\theta, \gamma=1)$

$X_1$ - единственное наблюдение $X$ имеет $f(x) = \frac{1}{\pi(1+(x-\theta)^2)}$

$$
\begin{matrix}
H_0: \theta = 0;\\
H_1: \theta = 1;
\end{matrix}
\begin{matrix}
\theta_0 = 0\\
\theta_1 = 1
\end{matrix}
\Rightarrow \frac{\frac{1}{\pi}\frac{1}{1+(x-1)^2}}{\frac{1}{\pi}\frac{1}{1+x^2}} = \frac{1+x^2}{x^2-2x+2}\geq c$$

Решим неравенство для нахождения критической области $c = 2$:

$$
T(\vec{x}) = \frac{1+x^2}{x^2-2x+2}\geq 2; \frac{-x^2+3x+x-3}{2+x^2-2x}\geq 0 \Rightarrow
$$

$$
x\in [1,3] \text{ - критическая область}
$$

$$F(X)=\frac{1}{\pi}\arctan(x-\theta)+\frac{1}{2}$$

$$
\alpha = P_{H_0}(T(\vec{x}) \in k_{\alpha}) = P_{H_0}(x\in [1,3]) = \frac{1}{\pi}\arctan(3)-\frac{1}{\pi}arctan(1)=\frac{1}{\pi}\arctan(3)-\frac{1}{4}
$$

$$
\beta = P_{H_0}(T(\vec{x})\notin k_{\alpha}) = P_{H_0}(x < 1) + P_{H_0}(x > 3) = \frac{1}{\pi}\arctan(0)+\frac{1}{2}+1-\frac{1}{\pi}\arctan(2)-\frac{1}{2}  =1-\frac{1}{\pi}\arctan(2)
$$
           """))


def solve_some_dificult_number_27():
    display(Markdown(r"""
$\frac{f\cdot S^2_w}{\sigma^2_w} \approx \chi^2(f) \begin{matrix}
\sigma^2_w \rightarrow \text{ несмещ. оценка } S^2_w\\
S^2_w = \frac{S^2_x}{n}+\frac{S^2_y}{m};
\end{matrix}$ 

Доказать: $\frac{1}{f} = \frac{1}{\sigma^4_w} \left(\frac{\sigma^4_x}{n^2(n-1)}+\frac{\sigma^4_y}{m^2(m-1)} \right)$

a) $Var(\frac{f\cdot S^2_w}{\sigma^2_w}) = Var(\chi^2(f)) = 2f$

$$
Var(\frac{f\cdot S^2_w}{\sigma^2_w}) = \frac{f^2}{\sigma^4_w}\cdot Var(S^2_w)=\frac{f^2}{\sigma^4_w}Var\left(\frac{1}{n^2}Var(S^2_x)+\frac{1}{m^2}Var(S^2_y)\right)
$$

б) $\frac{(n-1)S^2_x}{\sigma^2_x} \sim \chi^2(n-1)$

$Var(S^2_x) = \frac{2\sigma^4_x}{n-1} \Leftrightarrow Var(S^2_y)=\frac{2\sigma^4_y}{m-1}$ 

$Var\left(\frac{n-1}{\sigma^2_x}S^2_x\right) = 2(n-1); \frac{(n-1)^2}{\sigma^4_x}Var(S^2_x) = 2(n-1) \Rightarrow$

$$
\frac{f^2}{\sigma^4_w}\left(\frac{1}{n^2(n-1)} 2\sigma^4_x + \frac{1}{m^2(m-1)} 2\sigma^4_y\right) = 2f \text{ поделим все на } f^2
$$

$$
\frac{1}{f} = \frac{1}{\sigma^4_w} \left(\frac{\sigma^4_x}{n^2(n-1)}+\frac{\sigma^4_y}{m^2(m-1)} \right)
$$
           """))


def solve_some_dificult_number_28():
    display(Markdown(r"""
$\hat{f}(n,m)=\frac{\left(\frac{S^2_x}{n}+\frac{S^2_y}{m} \right)^2}{\frac{S^4_x}{n^2(n-1)}+\frac{S^4_y}{m^2(m-1)}} = \frac{\left(\frac{\frac{S^2_x}{S^2_y}}{n}+\frac{1}{m} \right)^2}{\frac{\frac{S^4_x}{S^4_y}}{n^2(n-1)}+\frac{1}{m^2(m-1)}} = \begin{Bmatrix}
\frac{S^2_x}{S^2_y} = t\\
\left(\frac{S^2_x}{S^2_y}\right)^2 = t^2
\end{Bmatrix} = \frac{\left(\frac{t}{n}+\frac{1}{m} \right)^2}{\frac{t^2}{n^2(n-1)}+\frac{1}{m^2(m-1)}} = f(t)$

$$
\frac{df}{dt} = \frac{2\left(\frac{t}{n} + \frac{1}{m} \right)}{n\left(\frac{t^2}{n^2(n-1)}+\frac{1}{m^2(m-1)} \right)}-\frac{2t\left(\frac{t}{n} + \frac{1}{m} \right)^2}{n^2(n-1)\left(\frac{t^2}{n^2(n-1)} + \frac{1}{m^2(m-1)} \right)^2}
$$

Приведем подобные и воспользуемся упрощением через библиотеку sympy:

$$
\frac{df}{dt} = 0 \Leftrightarrow \text{ Имеем два корня: } \begin{Bmatrix}
t = \frac{-n}{m}\\
t = \frac{n(n-1)}{m(m-1)}
\end{Bmatrix}
$$

Пользуясь методом интервалов находим точку максимума $\left(\frac{n(n-1)}{m(m-1)}\right)$

$$
f\left(\frac{n(n-1)}{m(m-1)} \right) = n+m-2
$$

$$
f\left(\frac{-n}{m} \right) = 0, \text{ если хотя бы 1 равен 1}
$$

В общем случае:

$$
min(n-1,m-1)\leq \hat{f} \leq n+m-2
$$
           """))


def solve_some_dificult_number_29():
    display(Markdown(r"""
$F(1,m) = \frac{\chi^2(1)}{\frac{\chi^2(m)}{m}} [\text{cdf Fisher(1;m)}];$ $T(m) = \frac{z}{\sqrt{\frac{\chi^2(m)}{m}}} [\text{cdf student(m)}]$; $\chi^2(m) = \sum^m_{i=1}z^2_i [\text{Z ∼ N(0;1),} \chi^2(1) = z^2] \Rightarrow$

$$
\Rightarrow F(1;m) = \frac{z^2}{\frac{\chi^2(m)}{m}} = \left(\frac{z}{\sqrt{\frac{\chi^2(m)}{m}}} \right)^2 = t^2(m)
$$

$$
P\left(F(1;m) \geq f_{\alpha}(1;m) \right) = \alpha
$$

$$
P\left(t^2(m) \geq t^2_{\frac{\alpha}{2}}(m) \right) = P\left(|t(m)| \geq |t_{\frac{\alpha}{2}}(m)| \right) = P\left(t(m) < -t_{\frac{\alpha}{2}}(m) \right) + P\left(t(m) > t_{\frac{\alpha}{2}}(m) \right) = 1 - (1-\frac{\alpha}{2})+\frac{\alpha}{2} = \alpha
$$
           """))


def solve_some_dificult_number_30():
    display(Markdown(r"""
В задаче описаны следующие события:
    
$A_1 - \{\text{обе котировки падают}\}$

$A_2 - \{\text{обе котировки растут}\}$

$A_3 - \{A\uparrow,B\downarrow\}$

$A_4 - \{A\downarrow,B\uparrow\}$

$H_0$:

| X  | A1   | A2   | A3   | A4   |
|----|------|------|------|------|
| Pi | 0,25 | 0,25 | 0,25 | 0,25 |

$H_1$: иначе.

Искомое частное распр. имеет вид:

| X  | A1   | A2   | A3   | A4   |
|----|------|------|------|------|
| ni | 26 | 25 | 29 | 20 |

$\sum_i n_i = 100 = n$

Заметим, что $n_i\cdot p_i \geq 5, \forall i = 1...4 \Rightarrow$ Воспользуемся $\chi^2$-критерием:

$$
\chi^2 - \sum^4_{k=1} \frac{\left(n_k - np_k \right)^2}{np_k} = \frac{(26-25)^2}{25}... = \frac{1+16+25}{25} = \frac{42}{25} = 1,68
$$

$$
\alpha = 1\% \Rightarrow \chi^2_{0,01}(4-1)=\chi^2_{0,01}(3) \approx 11,345; 1,68<11,345 \Rightarrow тут фото
$$

$$
\chi^2_{\text{набл}} \notin K_{\alpha} \Rightarrow H_0\text{ не отвергается}
$$
           """))


def solve_some_dificult_number_31():
    display(Markdown(r"""
$\alpha = 0,05 $, T - время ожидания

$H_0: T\sim U([0;10])$, $H_1: T\not\sim U([0;10])$

Будем использовать критерий Колмогорова:

$$
D_n\cdot sup\left(|\hat{F}_n(x)-F_x(x)| \right), где
$$

$\hat{F}_n(x)$ - выборочная функция распределения $\hat{F}_n(x) = \frac{1}{n}\sum^n_{k=1}I\{X_k \leq k\}$

$F_x(x)$ - $F_T(x)=\frac{x}{10}$

$k_{\alpha} = \sqrt{n}D_{набл}>C_{\alpha}$

| X   | F(x) | ^Fn(x)         |           \|^Fn(x)-F(x)\| |
|-----|------|----------------|-------------------------|
| 1,2 | 0,12 | 0,2            | 0,08                    |
| 3,7 | 0,37 | 0,4            | 0,03                    |
| 4,8 | 0,48 | 0,6            | 0,12                    |
| 5,1 | 0,51 | 0,8            | 0,29                    |
| 9,2 | 0,92 | 1              | 0,08                    |

$D_n = 0,29$

$\sqrt{5}\cdot 0,29 > C_{0,05} \rightarrow 1,35; \sqrt{n}D_{набл}<C_{0,05} \Rightarrow$

$H_0$ - не отвергается 
           """))


def solve_some_dificult_number_32():
    display(Markdown(r"""
$\exists$ 2 признака X,Y:

X - {оценка в школе}
Y - {оценка на экзамене}

$A_1$ - {'5'}, $A_2$ - {не '5'}

$H_0$: X,Y - независимые; $H_1$: X,Y - зависимые

Составим распределения для X, Y:

| X  | A1   | A2   |
|----|------|------|
| ni | 97   |  203 |

| Y  | A1   | A2   |
|----|------|------|
| nj | 48   |  252 |

Составим совместное распределение частот X и Y:

| X\\Y  | A1   | A2   |
|----|------|------|
| A1 | 18   |  79 |
| A2 | 30   |  173 |

Воспользуемся критерием $\chi^2$:

$$
\chi^2_{набл} = n\cdot \left[\sum_i \sum_j (\frac{n^2_{ij}}{n_i\cdot n_j}) - 1 \right] =
$$

$$
= 300\cdot \left[\frac{18^2}{97\cdot 48} + \frac{79^2}{252\cdot 97} + \frac{30^2}{48\cdot 203} + \frac{173^2}{203\cdot 252} - 1 \right] \approx 0,697
$$

$$
\chi^2_{\alpha=0,1}(2-1) = 2,705; 0,697<2,705 \Rightarrow
$$

$H_0$ не отвергается
           """))


def solve_some_dificult_number_33():
    display(Markdown(r"""
Восмпользуемся критерием Колмогорова:
    
$$
D_n = \sup|\hat{F}_{n1}(x)-\hat{F}_{n2}(x)|
$$

$$
\hat{F}_n(x) = \frac{1}{n}\sum^n_{k=1}I_{(X_k\leq x)}
$$

$H_0: F_1(x) = F_2(x)$

$H_1: F_1(x) \not= F_2(x)$

| оценка | 1 поток | 2 поток | ^Fn1(x) | ^Fn2(x) | \|^Fn1(x) - ^Fn2(x)\| |
|--------|---------|---------|---------|---------|-----------------------|
| 2      | 33      | 39      | 33/300  | 39/300  | 6/300                 |
| 3      | 43      | 35      | 76/300  | 74/300  | 2/300                 |
| 4      | 80      | 72      | 156/300 | 146/300 | 10/300                |
| 5      | 144     | 154     | 1       | 1       | 0                     |

$D_n = \frac{10}{300}$, $k_{\alpha}=\{\frac{\sqrt{n_1n_2}}{\sqrt{n_1+n_2}}\cdot D_n > C_{\alpha}\}$; $C_{\alpha} = 1,224$

$$
\frac{300}{\sqrt{600}} \frac{10}{300} > C_{\alpha} \Rightarrow H_0 \text{ не отвергается}
$$
           """))


def solve_some_dificult_number_34():
    display(Markdown(r"""
n = 395, $\alpha = 0,05$ $
\begin{matrix}
H_0: \text{событя независимы}\\
H_1: \text{событя зависимы}
\end{matrix} \Rightarrow
$

статистика критерия: $\chi^2_n = \sum^k_{i=1}\sum^m_{j=1}\frac{(V_{ij}-n\hat{p}_i\hat{q}_j)^2}{n\hat{p}_i\hat{q}_j}$

| Переключение\Возраст | 18-24 | 25-34 | 35-49 | 50-64 | Сумма |
|----------------------|-------|-------|-------|-------|-------|
| Да                   | 60    | 54    | 46    | 41    | 201   |
| Нет                  | 40    | 44    | 53    | 57    | 194   |
| Сумма                | 100   | 98    | 99    | 98    | 395   |

$$
\chi^2_n = \frac{(60-50,89)^2}{50,89} + \frac{(54-49,87)^2}{49,87} + \frac{(46-50,38)^2}{50,38} + \frac{(41-49,87)^2}{49,87} + \frac{(40-49,11)^2}{49,11} + \frac{(44-48,13)^2}{48,13} + \frac{(53-48,62)^2}{48,62} + \frac{(57-48,13)^2}{48,13} = 8,006
$$

$k_{\alpha} = \{\chi^2_n > \chi^2_{\alpha}((k-1)(m-1))\}$; $\chi^2_{\alpha} = \chi^2_{0,05} = 7,8148 \Rightarrow$

$$
\chi^2_n \in k_{\alpha} \Rightarrow H_0 \text{ отвергается }
$$

$$
\text{P-value} = P_{H_0}(\chi^2(3)>\chi^2_{набл}) = 1-F_{\chi^2(3)}(\chi^2_{набл}) = 0,046
$$
           """))




def equalsigma():
    display(Markdown(r"""
Воспользуемся $\chi^2$-критерием

1) Статистика критерия:

$$
\chi^2_0=\frac{1}{\sigma^2_0}\sum^n_{k=1}\left(X_k-\bar X\right)^2=\frac{(n-1)\delta^2}{\sigma^2_0}, \text{ где } \delta^2 = \frac{1}{n-1}\sum^n_{k=1}\left(X_k-\bar X \right)^2
$$

$$
K_{\alpha}, \text{ для } H_0: \sigma = \sigma_0; H_1: \sigma > \sigma_0: \chi^2_0 > \chi^2_{\alpha}(n-1)
$$

2) Если $H_0$ - верна, то с.в. $\chi^2 \sim \chi^2(n-1)$

$X_1,...,X_n \sim N(\mu;\sigma^2)$

$\chi^2=\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\bar X)^2 = \sum^n_{k=1}\left(\frac{X_k-\bar X}{\sigma_0} \right)^2 = \sum^n_{k=1}Z^2_k, \text{ где } Z_k = \frac{X_k=\bar X}{\sigma_0}$ 

a) $Cov(Z_i,Z_j)=-\frac{1}{n} (i\not=j)$

b) $Z_1+...+Z_n = 0$

c) $\sum^n_{k=1}(X_k-\mu)^2 = \sum^n_{k=1}(X_k-\bar X)^2 +n(\bar X[k=1] - \mu)^2$

3) Так как в силу вида $H_1 k_{\alpha}$ правостор., тогда P-значение - вероятность того, что основная статистика более экстремальной, чем наблюдаемое значение статистики, т.е

$$
pv(\bar x) = P\left(\chi^2_0 > \chi^2_{набл}(n) \right) = 1-P\left(\chi^2_0 < \chi^2_{набл}(n) \right) = F_{\chi^2_0}(\chi^2_{набл})
$$         """))

def equalsigmaless():
    display(Markdown(r"""
1) Воспользуемся следующим критерием:

$\chi^2=\frac{1}{\sigma^2_0}\cdot \sum^n_{k=1}(X_k-\bar X)^2$

$k_{\alpha}=\{\bar X \in \mathbb R^n | 0<\chi^2<\chi^2_{1-\alpha}(n-1)\}$

2) Если $H_0$ - верна, то $\chi^2 \sim \chi^2(n-1)$

Док-во:

$$
\chi^2 = \frac{1}{\sigma^2_0}\cdot \sum^n_{k=1}(X_k-\bar X)^2 = \frac{n-1}{\sigma^2_0}\cdot \frac{1}{n-1}\cdot \sum^n_{k=1}(X_k-\bar X)^2 = \frac{(n-1)S^2}{\sigma^2_0} \sim [\text{по теореме Фишера}] \chi^2(n-1)
$$

$P_{H_0}\left(T(X_1,....,X_n) \in k_{\alpha} \right) = P_{H_0}\left(\frac{1}{\sigma^2_0} \sum^n_{k=1}(X_k-\bar X)^2 \in (0;\chi^2_{1-\frac{\alpha}{2}}(n-1)) \cup (\chi^2_{\frac{\alpha}{2}}(n-1);+\inf) \right) = P_{H_0}\left(0<\chi^2(n-2)<\chi^2_{1-\frac{\alpha}{2}}(n-1) \right) + P_{H_0}\left(\chi^2(n-1)>\chi^2_{\frac{\alpha}{2}}(n-2) \right) = P\left(\chi^2(n-1)>0 \right) - P\left(\chi^2(n-1)>\chi^2_{1-\frac{\alpha}{2}}(n-1) \right)$

3) $Pvalue = 2min\{P_{H_0}\left(T(X_1,...,X_n)<\chi^2_{набл} \right); P_{H_0}\left(T(X_1,...,X_n)>\chi^2_{набл} \right) \} = 2min\{P\left(\chi^2(n-2) <\chi^2_{набл}\right ); P\left(\chi^2(n-2) >\chi^2_{набл}\right )\} = 2min\{F_{\chi^2(n-2)}\left(\frac{1}{\sigma^2_0} \sum^n_{k=1}(X_k-\bar X)^2 \right); 1-F_{\chi^2(n-1)}\left(\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k - \bar X)^2 \right) \}$ 
"""))

def bothsigmas():
    display(Markdown(r"""
1) Воспользуемся следующим критерием:

$\chi^2=\frac{1}{\sigma^2_0}\cdot \sum^n_{k=1}(X_k-\bar X)^2$

$k_{\alpha}=\{\bar X \in \mathbb R | \chi^2_{1-\frac{\alpha}{2}}(n-1)>\chi^2 \cup \chi^2>\chi^2_{\frac{\alpha}{2}}(n-1)\}, \text{ где } \chi^2_{\alpha}(n-1) - \text{ процентная точка уровня } \alpha \text{ для } \chi^2 \sim \chi^2(n-1)$

2) Если $H_0$ - верна, то $\chi^2 \sim \chi^2(n-1)$

Док-во:

$$
\chi^2 = \frac{1}{\sigma^2_0}\cdot \sum^n_{k=1}(X_k-\bar X)^2 = \frac{n-1}{\sigma^2_0}\cdot \frac{1}{n-1}\cdot \sum^n_{k=1}(X_k-\bar X)^2 = \frac{(n-1)S^2}{\sigma^2_0} \sim [\text{по теореме Фишера}] \chi^2(n-1)
$$

$P_{H_0}\left(T(X_1,....,X_n) \in k_{\alpha} \right) = P_{H_0}\left(\frac{1}{\sigma^2_0} \sum^n_{k=1}(X_k-\bar X)^2 \in (0;\chi^2_{1-\alpha}(n-1)) \right) = P_{H_0}\left(0<\chi^2(n-1)<\chi^2_{1-\alpha}(n-1) \right) = P(\chi^2(n-1)>0)-P(\chi^2(n-1)>\chi^2_{1-\alpha}(n-1)) = 1-(1-\alpha) = \alpha$

3) $Pvalue = P_{H_0}(T(X_1,...,X_n)<\chi^2_{набл}) = P_{H_0}\left(\frac{1}{\sigma^2_0}\sum^n_{k=1} (X_k-\bar X)^2 < \chi^2_{набл} \right) = P\left(\chi^2(n-2) < \chi^2_{набл} \right) = F_{\chi^2(n-1)}\left(\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\bar X)^2 \right)$
"""))

def musix():
    display(Markdown(r"""
1) Рассмотрим статистику:

$$
Z = \frac{\bar X - \bar Y}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}}; k_{\alpha} = \{\vec{X} \in \mathbb R^{n+m} | T\left(X_1,...,X_n,Y_1,...,Y_m \right) > Z_{\frac{\alpha}{2}} \}
$$

где $Z_{\frac{\alpha}{2}}$ - процентная точка стандартного ормального

2) Если $H_0$ - верна, то $\frac{\bar X - \bar Y}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}} \sim Norm(0,1)$

Док-во:

a) $\frac{1}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}}[\bar X - \bar Y]$ - линейнка комбинация нормальных распределений

б) $E\left(\frac{1}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}}[\bar X - \bar Y] \right) = \frac{1}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}}E\left([\bar X - \bar Y]\right) = \frac{\mu_X-\mu_Y}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}} = \{H_0: \mu_X=\mu_Y \} = 0$

в) $Var\left(\frac{1}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}}[\bar X - \bar Y] \right) = \frac{1}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}}[Var(\bar X) - Var(\bar Y)] = \frac{1}{\frac{\sigma^2_X}{n}+\frac{\sigma^2_Y}{m}}[\frac{\sigma^2_X}{n}+\frac{\sigma^2_Y}{m}] = 1$

Из 1,2,3 $\Rightarrow$, что $\frac{\bar X - \bar Y}{\sqrt{\frac{\sigma^2_X}{n} + \frac{\sigma^2_Y}{m}}} \sim Norm(0,1)$

$$
P_{H_0}\left(T(X_1,...,Y_m) \in k_{\alpha} \right) = P\left(|Z|>Z_{\frac{\alpha}{2}} \right) = P\left(Z>Z_{\frac{\alpha}{2}} \right) + P\left(Z<-Z_{\frac{\alpha}{2}} \right) = \frac{\alpha}{2} + \frac{\alpha}{2} = \alpha.
$$

3) $Pvalue = 2min\{P(Z<Z_{набл}); P(Z>Z_{набл}) \} = \{\text{ В случае четности плотности } Z\sim Norm(0,1) \} = 2F_Z(-|Z_{набл}|)= 1+2Ф_0(-|Z_{набл}|)$
"""))


def muisgreater():
    display(Markdown(r"""
1) Рассмотрим $T(X_1,...,X_n,Y_1,...,Y_m) = \frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}$; где $S = \frac{\sum^n_{k=1}(X_k-\bar X)^2 + \sum^m_{k=1}(Y_k-\bar Y)^2}{n+m-2}$

$$
k_{\alpha} = \{\vec{X} \in \mathbb R^{n+m} |  \frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} > t_{\alpha}(m+n-2)\}
$$

2) Если $H_0$ - верна, то $\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} \sim T(n+m-2)$

Док-во:

a) $\frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} / \frac{S}{\sigma}; \frac{1}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}[\bar X - \bar Y]$ - линейная комбинация нормальных распределений.

б) $E[\frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}] = \frac{1}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}E[\bar X - \bar Y] = \{H_0 - верна \} = 0$

в) $Var[\frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}] = \frac{1}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}[Var(\bar X) - Var(\bar Y)] = \frac{m\cdot n}{\sigma^2\cdot (m+n)}\cdot [\frac{\sigma^2}{n}+\frac{\sigma^2}{m}] = 1$

из 1,2,3 $\Rightarrow$, что $\frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} = Z\sim Norm(0,1)$

г) $\frac{S^2}{\sigma^2} = \frac{m+n-2}{\sigma^2}\cdot \frac{S^2}{n+m-2}; \frac{m+n-2}{\sigma^2}\cdot S^2 = \frac{1}{\sigma^2} \sum^n_{k=1}(X_k-\bar X)^2 + \frac{1}{\sigma^2}\sum^m_{k=1}(Y_k-\bar Y)^2 =\{\text{Пользуясь теоремой Фишера} \} = \chi^2(n-1)+\chi^2(m-1)=\chi^2(n+m-2)$

д) Итак, $\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} = \frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} / \frac{S}{\sigma} = \frac{Z}{\sqrt{\frac{\chi^2(n+m-2)}{n+m-2}}}\sim T(n+m-2)$

$$
P_{H_0}\left(\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} \in k_{\alpha} \right) = P\left(T>t_{\alpha}(n+m-2) \right) =^{def} \alpha
$$

3) $Pvalue = P_{H_0}\left(\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}>t_{набл} \right) = P\left(T>t_{набл} \right) = 1 - P\left(T\leq t_{набл} \right) = 1 - F_{t(n+m-2)}(t_{набл})$
"""))

def muisgreater():
    display(Markdown(r"""
1) Рассмотрим $T(X_1,...,X_n,Y_1,...,Y_m) = \frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}$; где $S = \frac{\sum^n_{k=1}(X_k-\bar X)^2 + \sum^m_{k=1}(Y_k-\bar Y)^2}{n+m-2}$

$$
k_{\alpha} = \{\vec{X} \in \mathbb R^{n+m} |  \frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} > t_{\frac{\alpha}{2}}(m+n-2)\}
$$

2) Если $H_0$ - верна, то $\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} \sim T(n+m-2)$

Док-во:

a) $\frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} / \frac{S}{\sigma}; \frac{1}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}[\bar X - \bar Y]$ - линейная комбинация нормальных распределений.

б) $E[\frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}] = \frac{1}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}E[\bar X - \bar Y] = \{H_0 - верна \} = 0$

в) $Var[\frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}] = \frac{1}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}}[Var(\bar X) - Var(\bar Y)] = \frac{m\cdot n}{\sigma^2\cdot (m+n)}\cdot [\frac{\sigma^2}{n}+\frac{\sigma^2}{m}] = 1$

из 1,2,3 $\Rightarrow$, что $\frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} = Z\sim Norm(0,1)$

г) $\frac{S^2}{\sigma^2} = \frac{m+n-2}{\sigma^2}\cdot \frac{S^2}{n+m-2}; \frac{m+n-2}{\sigma^2}\cdot S^2 = \frac{1}{\sigma^2} \sum^n_{k=1}(X_k-\bar X)^2 + \frac{1}{\sigma^2}\sum^m_{k=1}(Y_k-\bar Y)^2 =\{\text{Пользуясь теоремой Фишера} \} = \chi^2(n-1)+\chi^2(m-1)=\chi^2(n+m-2)$

д) Итак, $\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} = \frac{\bar X - \bar Y}{\sigma\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} / \frac{S}{\sigma} = \frac{Z}{\sqrt{\frac{\chi^2(n+m-2)}{n+m-2}}}\sim T(n+m-2)$

$$
P_{H_0}\left(\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n}+\frac{1}{m}}} \in k_{\alpha} \right) = P\left(|T|>t_{\frac{\alpha}{2}}(n+m-2) \right) = P\left(T<-t_{\frac{\alpha}{2}}(n+m-2) \right) + P\left(T>t_{\frac{\alpha}{2}}(n+m-2) \right) = 1- P\left(T>t_{1-\frac{\alpha}{2}}(n+m-2) \right) + \frac{\alpha}{2} = 1 - 1 + \frac{\alpha}{2} + \frac{\alpha}{2} = \alpha
$$

3) $Pvalue = 2min\left(P_{H_0}\left(\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n} + \frac{1}{m}}} < t_{набл} \right);P_{H_0}\left(\frac{\bar X - \bar Y}{S\cdot \sqrt{\frac{1}{n} + \frac{1}{m}}} > t_{набл} \right)  \right) = 2min\left(F_{t(n+m-2)}(t_{набл}); 1-(F_{t(n+m-2)}(t_{набл}) \right) = 2P\left(T(n+m-2)\leq-|t_{набл}| \right) = 2F_{t(n+m-2)}(-|t_{набл}|) = 2F_{t(n+m-2)}\left(-\frac{|\bar X - \bar Y|}{S^2\sqrt{\frac{1}{n}+ \frac{1}{m}}} \right)$
"""))

def behrensfisher():
    display(Markdown(r"""
1) Рассмотрим статистику Уэлча:

$$
T(X_1,...,Y_m) = \frac{\bar X - \bar Y}{\sqrt{\frac{1}{n(n-1)}\sum^n_{k=1}(X_k-\bar X)^2+\frac{1}{m(m-1)}\sum^m_{k=1}(Y_k-\bar Y)^2}}; \hat{f} = \frac{\left(\frac{S^2_X}{S^2_Y}+\frac{n}{m} \right)^2}{\frac{1}{n-1}\cdot \frac{S^2_X}{S^2_Y} + \frac{1}{m-1}(\frac{n}{m})^2}
$$

$$
k_{\alpha} = \{\vec{x} \in \mathbb R^{n+m} ||T(X_1,...,Y_m)|>t_{\frac{\alpha}{2}}(\hat{f}) \}; t_{\frac{\alpha}{2}}(\hat f) - \text{ процентная точка распределения стьюдента с дробным числом степеней свободы}
$$

2) Если $H_0$ - верна, то $T\left(X_1,...,Y_m\right) \approx t(\hat f)$ - т.е. Статистика ведет себя как распределение Стьюдента с числом свободы f.

$
f = \frac{\left(\frac{\sigma^2_X}{\sigma^2_Y}+\frac{n}{m} \right)^2}{\frac{1}{n-1}\cdot \frac{\sigma^2_X}{\sigma^2_Y} + \frac{1}{m-1}(\frac{n}{m})^2}
$

3) $Pvalue = 2min\left(P_{H_0}(T(X_1,...,Y_m)>t_{набл}); P_{H_0}(T(X_1,...,Y_m)<t_{набл}) \right)= \{\text{ в силу четности плотности и если взять t_набл по модулю, то min сохраняется и при этом обязательнго равны } \} = 2min\left(P_{H_0}(T(X_1,...,Y_m)>|t_{набл}|); P_{H_0}(T(X_1,...,Y_m)<-|t_{набл}|)\right) = 2P_{H_0}\left(T(X_1,...,Y_m) <-|t_{набл}| \right) = 2F_{t(\hat f)}(-|t_{набл}|)$
"""))

def sigmaequalgreat():
    display(Markdown(r"""
1) Рассмотрим F-статистику:

$$
T(X_1,...,Y_m) = \frac{S^2_X}{S^2_Y} = \frac{\frac{1}{n-1}\sum^n_{k=1}\left(X_k-\bar X \right)^2}{\frac{1}{m-1}\sum^m_{k=1}\left(Y_k-\bar Y \right)^2}
$$

$$
k_{\alpha} = \{\vec{X} \in R^{n+m} | T(X_1,...,Y_m)>f_{\alpha}(n-1;m-1) \}, \text{ где } f_{\alpha}(n-1;m-1) \text{ - процентная точка распределения Фишера}
$$

2) Если $H_0$ - верна, то $\frac{S^2_X}{S^2_Y}\sim F(n-1;m-1)$

Док-во:

$$
\frac{S^2_X}{S^2_Y} = \frac{\frac{n-1}{\sigma}S^2_X\cdot \frac{1}{n-1}}{\frac{m-1}{\sigma}S^2_Y\cdot \frac{1}{m-1}} = \frac{\chi^2(n-1)}{\chi^2(m-1)}\cdot \frac{m-1}{n-1} =^{def}F\sim F(n-1;m-1) \text{ чтд }
$$


$P_{H_0}\left(T(X_1,...,Y_m) \in k_{\alpha} \right) = \alpha$

Док-во:

$$
P\left(\frac{S^2_X}{S^2_Y} > f_{\alpha}(n-1;m-1) \right) = P\left(F_{n-1;m-1} > f_{\alpha}(n-1;m-1)\right) =^{def} \alpha
$$

3)$Pvalue = \mathbb P_{H_0}\left(T(X_1,...,Y_m) > \mathbb F_{набл} \right) = 1-\mathbb P\left(\mathbb F\leq \mathbb F_{набл} \right) = 1-F_{\mathbb F(n-1;m-1)}\left(\frac{S^2_X}{S^2_Y} \right)$
"""))

def sigmaequalsix():
    display(Markdown(r"""
1) Рассмотрим F-статистику:

$$
T(X_1,...,Y_m) = \frac{S^2_X}{S^2_Y} = \frac{\frac{1}{n-1}\sum^n_{k=1}\left(X_k-\bar X \right)^2}{\frac{1}{m-1}\sum^m_{k=1}\left(Y_k-\bar Y \right)^2}
$$

$$
k_{\alpha} = \{\vec{X} \in R^{n+m} | T(X_1,...,Y_m) \in (0;f_{1-\frac{\alpha}{2}}(n-1;m-1))\cup(f_{\frac{\alpha}{2}}(n-1,m-1);+\infty) \}, \text{ где } f_{\alpha}(n-1;m-1) \text{ - процентная точка распределения Фишера}
$$

2) Если $H_0$ - верна, то $\frac{S^2_X}{S^2_Y}\sim F(n-1;m-1)$

Док-во:

$$
\frac{S^2_X}{S^2_Y} = \frac{\frac{n-1}{\sigma}S^2_X\cdot \frac{1}{n-1}}{\frac{m-1}{\sigma}S^2_Y\cdot \frac{1}{m-1}} = \frac{\chi^2(n-1)}{\chi^2(m-1)}\cdot \frac{m-1}{n-1} =^{def}F\sim F(n-1;m-1) \text{ чтд }
$$


$\mathbb P_{H_0}\left(T(X_1,...,Y_m) \in k_{\alpha} \right) = \alpha$

Док-во:

$$
\mathbb P\left(\frac{S^2_X}{S^2_Y} \in (0;f_{1-\frac{\alpha}{2}}(n-1;m-1))\cup (f_{\frac{\alpha}{2}}(n-1;m-1);+\infty) \right) = \mathbb P\left(\mathbb F<f_{1-\frac{\alpha}{2}} \right) + \mathbb P\left(\mathbb F>f_{1-\frac{\alpha}{2}} \right) = 1-\mathbb P(\mathbb F > f_{1-\frac{\alpha}{2}}) + \mathbb P(\mathbb F > f_{\frac{\alpha}{2}}) = 1-1+\frac{\alpha}{2}+\frac{\alpha}{2} = \alpha
$$

3)$Pvalue = 2min\left(\mathbb P_{H_0}(T(X_1,...,Y_m)>\mathbb F_{набл}); \mathbb P_{H_0}(T(X_1,...,Y_m)<\mathbb F_{набл}) \right) = 2min\{1- \mathbb P(\mathbb F\leq \mathbb F_{набл}); \mathbb P(\mathbb F \leq \mathbb F_{набл}) \} = 2min\{(1-F_{\mathbb F(n-1;m-1)}(\frac{S^2_X}{S^2_Y}); F_{\mathbb F(n-1;m-1)}(\frac{S^2_X}{S^2_Y})) \}$
"""))

def studentnm2():
    display(Markdown(r"""
1) $T(X_1,...,Y_m) = \mathbb F = \frac{MSTR}{MSE} = \frac{\frac{SSTR}{(2-1)}}{\frac{SSE}{n+m-2}} = \frac{(\bar X - \bar Y)^2}{S^2_p(\frac{1}{n}+\frac{1}{m})} = \mathbb T^2$ - статистика в квадрате

где $S^2_p = \frac{1}{n+m-2}\left((n-1)S^2_X+(m-1)S^2_Y \right)$

$$
k_{\alpha} = \{\vec{X} \in \mathbb R^{n+m} | T(X_1,...,Y_m) > f_{\alpha}(1;n+m-2) \}
$$

2) $\mathbb P \left(\mathbb F > f_{\alpha}(1;n+m-2) \right) = \{n+m-2 = a \} = \mathbb P\left(\frac{\chi^2(1)\cdot a}{\chi^2(a)}>f_{\alpha}(1;a) \right) = \mathbb P\left(\frac{\mathcal{Z}^2}{\frac{1}{a}\sum^a_{k=1}\mathcal Z^2_k}> f_{\alpha}(1;a) \right) = \mathbb P\left(\frac{|\mathcal Z|}{\sqrt{\frac{1}{a}\sum^a_{k=1}\mathcal Z^2_k}} > \sqrt{f_{\alpha}(1;a)} \right) = \mathbb P\left(-\sqrt{f_{\alpha}(1;a)}<\frac{\mathcal Z}{\sqrt{\frac{1}{a}\sum^a_{k=1}\mathcal Z^2_k}} < \sqrt{f_{\alpha}(1;a)} \right) = $

$\begin{matrix}
\mathbb P\left(-\sqrt{f_{\alpha}(1;a)} < t < \sqrt{f_{\alpha}(1;a)}\right) = \alpha\\
\mathbb P\left(-t_{\frac{\alpha}{2}}(a) < t < t_{\frac{\alpha}{2}}(a) \right) = \alpha
\end{matrix} \Rightarrow \{\text{ в силу монотонности } \} \begin{matrix}
F^{-1}_{t}(x)\\
\sqrt{f_{\alpha}(1;a)}=t_{\frac{\alpha}{2}}(a)
\end{matrix} \Rightarrow$

$$
f_{\alpha}(1;n+m-2) = t^2_{\frac{\alpha}{2}}(n+m-2)
$$
"""))
def pearsoncriteria():
    display(Markdown(r"""
1) Выборки $X_1,...,X_n$ называется однородными, если они распределены одинаковы, т.е. $F_{X_1}=F_{X_2}=...=F_{X_n}$
2) Статистика: $T(\vec{X_1},...,\vec{X_n}) = \chi^2_0 = n\cdot \left((\sum^l_{i=1}\frac{1}{\nu_i}\cdot \sum^k_{j=1}\frac{\nu^2_{ij}}{n_j})-1 \right)$

$$
k_{\alpha} = \{\vec X \in \mathbb R^n | \chi^2_0 > \chi^2_{\alpha}\left((k-1)\cdot(l-1) \right) \}
$$
3) Однородность двух выборок:
$m = \sum^l_{i=1}\alpha_i = \sum^l_{i=1}\nu_{i1}$

$n = \sum^l_{j=1}\beta_j = \sum^l_{j=1}\nu_{j2}$

$n_1 = m; n_2 = n$

$$
\chi^2_0=N\left((\sum^l_{i=1}\frac{1}{\nu_i}\sum^2_{j=1}\frac{\nu^2_{ij}}{n_j}) - 1 \right)
$$
"""))

def conttablechi():
    display(Markdown(r"""
1) Пусть $\hat p_i = \frac{\alpha_i}{n}; \hat q_j=\frac{\beta_j}{n}$

Тогда статистика:

$$
\chi^2_H = \sum^n_{i=1}\sum^m_{j=1}\left(\frac{(\nu_{ij}-n\hat p\hat q)^2}{n\hat p \hat q} \right) = \sum^n_{i=1}\sum^m_{j=1}\left(\frac{(\nu_{ij}-\frac{\alpha_i\beta_i}{n})^2}{\frac{\alpha_i\beta_i}{n}} \right)
$$

Если $H_0$ - верна, т. е. $\mathbb P\left(X \in A_{j}; Y \in B_i \right) = \mathbb P\left(X \in A_j \right)\cdot \mathbb P \left(Y \in B_i \right)$, то $\chi^2_H \rightarrow^d \chi^2((k-1)(m-1))$

$$
k_{\alpha} = \{\vec{X} \in \mathbb R^n | \chi^2_H > \chi^2_{\alpha}((k-1)(m-1)) \}
$$

2) $chi^2_H = n\cdot \left(\frac{a^2}{(a+c)(a+b)}+\frac{b^2}{(b+d)(a+b)}+\frac{c^2}{(a+c)(c+d)}+\frac{d^2}{(b+d)(c+d)}-1 \right) = \{\text{ решим уравнение с помощью библиотеки sympy } \} = \frac{n(ad-bc)^2}{(a+b)(a+c)(b+d)(c+d)}$
from sympy.abc import a,b,c,d,n
from sympy import expand, simplify, collect, factor

d = n*(a**2/((a+c)*(a+b))+b**2/((b+d)*(a+b))+c**2/((a+c)*(c+d))+d**2/((b+d)*(c+d)))
d = expand(d)
d
"""))

def solve_another_strange_number_1():
    display(Markdown(r"""
Статистической гипотезой называется любое утверждение о виде или параметрах генерального
распределения. 

Статистическая гипотеза называется параметрической, если она основана на предположении, что генеральное распределение известно с точностью до конечного числа параметров.   

Параметрическая гипотеза называется простой, если она имеет вид: $\theta = \theta_0$ , где $\theta_0$ – некоторое фиксированное начение параметра . Гипотеза вида:$\theta \in \Theta $ где $\Theta$  – какое-либо множество, содержащее, по меньшей мере, два различных элемента, называется сложной.


H0 - основная гипотеза H1- альтернативная гипотеза 

$ K_\alpha $ -критичесая область $ K_\alpha \in R^n$

$ T(X_1,..X_n)$ - статистка критерия

Гипотеза H0 отвергается, если $ T(X_1,..X_n) \in R^n $ и принимается, если $ T(X_1,..X_n) \notin R^n $. Критические области обычно задаются как односторонние или двусторонние.

$ K_\alpha = \{(X_1,..X_n) \in R^n : T(X_1,..X_n)<c_1\} $  
$ K_\alpha = \{(X_1,..X_n) \in R^n : T(X_1,..X_n)>c_2\} $  
$ K_\alpha = \{(X_1,..X_n) \in R^n : T(X_1,..X_n)<c_1 \cup  T(X_1,..X_n)<c_1 \}  $  

$ c_1 и c_2 $ - критические значения  

Если H0-верна, но отвергается, то это ошибка I рода. Вероятность этой ошибки назывется уровнем знчимости $\alpha$   

Если H1-верна, но отвергается, то это ошибка II рода. Вероятность этой ошибки  $\beta; W = 1 - \beta$ - мощбность критерия  

Схема:  
1) Сформировать Н0, H1, $\alpha$  
2) Найти $ c_1 ; c_2 ; K_\alpha $  
3) Вычислить $ T(X_1,..X_n)$ и проверить, что $ T(X_1,..X_n) \in K_\alpha $  
4) Сделать вывод
    """))

def solve_another_strange_number_2():
    display(Markdown(r"""
1) Пусть $ X \sim Norm(\theta, \sigma^2)$  
$ H0 = \theta_0$  
$ H1 = \theta_1$  
$ \theta_1 > \theta_0 \Rightarrow  K_\alpha \in (c_\alpha;+\infty)$  
Eсли H0 - верна то $ \bar{X} \sim  Norm(\theta, \frac{\sigma^2}{n})$  
$\alpha = P(\bar{X}>c_\alpha) = 1 - P(\bar{X} \leq c_\alpha) = 1 - P(\frac{\bar{X}-\theta_0}{\sigma}\sqrt{n} \leq \frac{c_\alpha-\theta_0}{\sigma}\sqrt{n}) = \{ \frac{\bar{X}-\theta_0}{\sigma}\sqrt{n} \sim Norm(0,1) \} = 1 - F_z(\sqrt{n}\frac{c_\alpha-\theta_0}{\sigma})$  
$F^{-1}_\alpha(1-\alpha) = \sqrt{n}\frac{c_\alpha-\theta_0}{\sigma}$  
$ Z_{1-\alpha}=\sqrt{n}\frac{c_\alpha-\theta_0}{\sigma}$  
$c_\alpha = \theta_0 + Z_{1-\alpha}\frac{\sigma}{\sqrt{n}}$  
2) Если $\alpha$ - веротянотсь ошибки I рода - $P(\bar{X} > c_\alpha)$ - вероятнотсь попадания в $ K_\alpha$  
3) Если $\bar{X}<c_\alpha$, мы не отвргаем H0 и при это H1 верно, то мы соврешаем ошибку II рода $\beta = P_{H1}=(\bar{X}<c_\alpha)-P(\frac{\bar{X}-\theta_1}{\sigma}\sqrt{n} \leq \frac{c_\alpha-\theta_1}{\sigma}\sqrt{n}) =\{ \frac{\bar{X}-\theta_1}{\sigma}\sqrt{n} \sim Norm(0,1) \} = F_z(\frac{c_\alpha-\theta_1}{\sigma})\sqrt{n}$  
Вероятноть попадания  в R \ $K_\alpha$   

4) $\alpha + \beta \rightarrow \min$  
$ f = 1 - F_Z(\frac{c_\alpha - \theta_0}{\sigma}\sqrt{n}) + F_z(\frac{c_\alpha - \theta_1}{\sigma}\sqrt{n}) =  1 - F_Z(Z_{1-\alpha}) + F_Z(Z_{1-\alpha}+ \frac{\theta_0-\theta_1}{\sigma}\sqrt{n}) = \{ \frac{\theta_0-\theta_1}{\sigma}\sqrt{n} = a \} = 1 - F_Z(Z_{1-\alpha})+F_Z(Z_{1-\alpha}+a)$ Переменная здесь $ Z_{1-\alpha}=Z$


$ f'_z = -\phi(Z) + \phi(Z+a)= 0$  
$ \phi(Z)  = \phi(Z+a) ,$ где $\phi(x)=\frac{1}{\sqrt{2\pi}}\exp^{\frac{-x^2}{2}}$  
$ \frac{1}{\sqrt{2\pi}}\exp^{\frac{-(Z+\alpha)^2}{2}} = \frac{1}{\sqrt{2\pi}}\exp^{\frac{-(Z)^2}{2}}$ 


$ (Z+\alpha)^2 = Z^2$  
$ (Z + \alpha -Z)(Z + \alpha +Z) =0$  
$ Z=\frac{-\alpha}{2}$  
$ Z_{1-\alpha} = \frac{-\alpha}{2}$  


$ \frac{c_\alpha-\theta_0}{\sigma}\sqrt{n} = -\frac{\theta_0-\theta_1}{1\sigma}\sqrt{n}$

$c_\alpha = \frac{\theta_1-\theta_0}{2}+\theta_0 = \frac{\theta_1+\theta_0}{2}$

Для данной ситуации $\alpha + \beta \rightarrow \min$ если $c_\alpha = \frac{\theta_1+\theta_0}{2}$
    """))

def solve_another_strange_number_3():
    display(Markdown(r"""
1) Критерий назывется несмещенным, если  $W(\theta)\geq\alpha,  \forall  \theta \in \Theta_1 $ т.е правильно еотверждение Н0 не менее вероятно чем неправильное  

2) Критерий назывется состоятельным, если $ \forall  \theta \in \Theta_1 , W(\theta) \longrightarrow 1,$ при $n \rightarrow \infty$

3) $ W(\mu) = \frac{1}{2}-\Phi_0(z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)), \mu \in (\mu_0; +\infty)    $ Проверим, что $W(\mu)  \leq \alpha$ 

$\frac{1}{2} -\Phi_0(z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)) \leq \alpha $  
$\Phi_0(z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)) \leq \frac{1}{2} - \alpha | + \frac{1}{2} $   
$\frac{1}{2} + \Phi_0(z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)) \leq 1 - \alpha $

$F_z(z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)) \leq 1 - \alpha)$  

$\{P(Z >Z_\alpha) = 1 - F_z(Z_\alpha)=\alpha$  
$ F_z(Z_\alpha) = 1-\alpha$  
$ Z_\alpha = F^{-1}_Z(1-\alpha)\}$


$F_z(z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)) \leq 1 - \alpha) |F^{-1}_Z$

$ z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)  \leq z_\alpha $

$ z_\alpha - z_\alpha \leq\frac{\sqrt{n}}{\sigma}(\mu-\mu_0)  $

$ 0 \leq \frac{\sqrt{n}}{\sigma}(\mu-\mu_0) | :\frac{\sqrt{n}}{\sigma} $

$ 0 \leq \mu-\mu_0 $  

$\mu_0 \leq \mu$ - вернно $ \forall \mu \in (\mu_0; +\infty) \Rightarrow $ критерий несмещенный


Проверим что $ W(\theta) \longrightarrow 1,$ при $n \rightarrow \infty$

$ \lim\limits_{n\to\infty}(\frac{1}{2}-\Phi_0(z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)) =  \frac{1}{2}-\lim\limits_{n\to\infty}(\Phi_0(z_\alpha - \frac{\sqrt{n}}{\sigma}(\mu-\mu_0)) = $

$ \{-\frac{\sqrt{n}}{\sigma}(\mu-\mu_0)) \longrightarrow +\infty \}$

$ = \frac{1}{2} - \frac{1}{\sqrt{2\pi}} \int_{0}^{-\infty} \exp^{\frac{-x^2}{2}}dx = \frac{1}{2} - (-\frac{1}{2}) = 1 \Rightarrow  $ критерий состоятельнй
    """))

def solve_another_strange_number_4():
    display(Markdown(r"""
Лемма Неймана-Пирсона - Наиболее мощьный критерий проверки Н0 против Н1 существует и имеет критическую область $$ K_\alpha = \{(x_1,...,x_n) | \frac{\prod_{i=1}^n f(x_1,\theta_1)}{\prod_{i=1}^n f(x_1,\theta_0)}  \geq c \}$$

$T(\overrightarrow{X}) =  \frac{\prod_{i=1}^n f(x_1,\theta_1)}{\prod_{i=1}^n f(x_1,\theta_0)}$ - статистика правдоподобия  

II) Пусть $ X = (X_1,..,X_n)$ - выборка обьема n 

$ X_1  \thicksim Norm(\theta, \sigma^2)  $  

$ H0 : \theta = \theta_0$  
$ H1 : \theta = \theta_1  ;  \theta_1> \theta_0 $ 

$\theta$ - неизвестно, $\sigma^2$ - известа  

   1) Рассмотрим $$ T(X_1,...,X_n) = \frac{\prod_{i=1}^n f(x_1,\theta_1)}{\prod_{i=1}^n f(x_1,\theta_0)}= \frac{\prod_{i=1}^n\frac{1}{\sigma\sqrt{2\pi}}\exp^{-\frac{(X_i-\theta_1)^2}{2\sigma^2}}}{\prod_{i=1}^n \frac{1}{\sigma\sqrt{2\pi}}\exp^{-\frac{(X_i-\theta_0)^2}{2\sigma^2}}} = \exp ^{\sum_{i=1}^n [- \frac{X_i-\theta_1)^2}{2\sigma^2} + \frac{X_i-\theta_0)^2}{2\sigma^2}]}=$$

$$ = \exp^{\frac{1}{2\sigma^2}\sum_{i=1}^n(-(X_i)^2+2X-i\theta_1-(\theta_1)^2+(X_i)^2-2X_i\theta_0+(\theta_0)^2)} = \exp^{\frac{1}{2\sigma^2}\sum_{i=1}^n(2X_i(\theta_1-\theta_0)+(\theta_0-\theta_1)^2)} = \exp^{\frac{\theta_1-\theta_0}{\sigma^2}\bar{X}n+\frac{(\theta_0)^2-(\theta_1)^2}{\sigma^2}n}$$


$$ 2) K_\alpha = \{ \overrightarrow{x} \in R^n | T(x) > c \} = \{\bar{x} \in R^n |\exp^{\frac{\theta_1-\theta_0}{\sigma^2}\bar{X}n+\frac{(\theta_0)^2-(\theta_1)^2}{\sigma^2}n} >c\} = \{\bar{x} \in R^n | \frac{\theta_1-\theta_0}{\sigma^2}\bar{X}n+\frac{(\theta_0)^2-(\theta_1)^2}{\sigma^2}n > \ln{c} \} = \{ \bar{x} \in R^n | \bar{X} > \frac{2\sigma^2\ln{c}-(\theta_0^2-\theta_1^2)n}{2\sigma^2}\cdot\frac{\sigma^2}{(\theta_0-\theta_1)n} \} $$  


3) $K_\alpha$ определяется так: $  K_\alpha = \{\bar{x} \in R^n |\bar{x} > \frac{\sigma}{\sqrt{n}} z_\alpha+\theta_0\}$ 

$$ \frac{\theta_1+\theta_0}{2} + \frac{\sigma^2\ln{c}}{(\theta_1-\theta_0)n} = \frac{\sigma}{\sqrt{n}} z_\alpha+\theta_0$$


$$ \ln(c) = \frac{z_\alpha(\theta_1-\theta_0)\sqrt{n}}{\sigma}+\frac{n(\theta_0^2-\theta_1^2)}{2\sigma^2}$$


$$ c = \exp(\frac{z_\alpha(\theta_1-\theta_0)\sqrt{n}}{\sigma}+\frac{n(\theta_0^2-\theta_1^2)}{2\sigma^2}) $$

При выборе такого с области эквивалентны, следовательно критерий наиболее мощный
    """))

def solve_another_strange_number_5():
    display(Markdown(r"""
1) Выберем Z-статистику: $ Z = \frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}$  

Критическое множество: $ K_\alpha = \{\bar{X} \in R^n | \frac{\bar{X}-\mu_0}{\sigma}\sqrt{n} > Z_\alpha\}$  

Где $Z_\alpha$ такое число, что $P(Z>Z_\alpha) = \alpha; Z \sim Norm(0,1)$  

2) 1. Если Н0 верна, то $ Z \sim Norm(0,1) $ 

Док-во $ \frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)$ -сумма нормальный распределений нормальное распределение 

$ E[\frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)] =\frac{\sqrt{n}}{\sigma}(E[\frac{1}{n}\sum^n_{i=1}(X_i)]-\mu_0) = \frac{\sqrt{n}}{\sigma}(\mu_0-\mu_0) = 0 $ 

$Var(\frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)) = \frac{n}{\sigma^2}Var(\frac{1}{n}\sum^n_{i=1}X_i - \mu_0) =\frac{n}{\sigma^2} \frac{\sum^n_{i=1}X_i}{n^2} = 1 $ (в силу независимости)  

2. $ Z \sim Norm(0,1)$, тогда $ K_\alpha = \{\bar{X} \in R^n | Z>Z_\alpha \} $  

Док-во $ P(\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n} > Z_\alpha)$ (если Н0 - верна) $ P(Z>Z_\alpha)=\{Z \sim Norm(0,1) \} = \alpha$ 

3) $Pvalue = P(Z>Z_{набл}) = 1 - P(Z \leq Z_{набл}) = 1 - (\frac{1}{2}+ \Phi_0(Z_{набл})) = \frac{1}{2} - \Phi_0(\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}) $, где $\Phi_0$ - Функция Лапласа
    """))

def solve_another_strange_number_6():
    display(Markdown(r"""
1) Выберем Z-статистику: $ Z = \frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}$  

Критическое множество: $ K_\alpha = \{\bar{X} \in R^n | \frac{\bar{X}-\mu_0}{\sigma}\sqrt{n} < -Z_\alpha\}$  

Где $Z_\alpha$ такое число, что $P(Z>Z_\alpha) = \alpha; Z \sim Norm(0,1)$  

2) 1. Если Н0 верна, то $ Z \sim Norm(0,1) $ 

Док-во $ \frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)$ -сумма нормальный распределений нормальное распределение 

$ E[\frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)] =\frac{\sqrt{n}}{\sigma}(E[\frac{1}{n}\sum^n_{i=1}(X_i)]-\mu_0) = \frac{\sqrt{n}}{\sigma}(\mu_0-\mu_0) = 0 $ 

$Var(\frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)) = \frac{n}{\sigma^2}Var(\frac{1}{n}\sum^n_{i=1}X_i - \mu_0) =\frac{n}{\sigma^2} \frac{\sum^n_{i=1}X_i}{n^2} = 1 $ (в силу независимости)   

2. $ Z \sim Norm(0,1)$, тогда $ K_\alpha = \{\bar{X} \in R^n | Z<-Z_\alpha\}$  

Док-во $ P(\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n} < Z_\alpha)$ (если Н0 - верна) $= P(Z< -Z_\alpha)= \{Z \sim Norm(0,1) \} = 1 - P(Z>-Z_\alpha)= \{-Z_\alpha = Z_{1-\alpha}\} = 1 - P(Z>Z_{1-\alpha}) = 1 - (1-\alpha) = \alpha$  

3) $Pvalue = P(T(X_1,.., X_n)<Z_{набл}) = P(Z<Z_{набл})  = \frac{1}{2} + \Phi_0(\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}) $, где $\Phi_0$ - Функция Лапласа


    """))

def solve_another_strange_number_7():
    display(Markdown(r"""
1) Выберем Z-статистику: $ Z = \frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}$  

Критическое множество: $ K_\alpha = \{\bar{X} \in R^n | \left\lvert\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}\right\rvert < Z_{\frac{\alpha}{2}}\}$  

Где $Z_\alpha$ $ - процентная точка стандартоного норального распределения  

2) 1. Если Н0 верна, то $ Z \sim Norm(0,1) $ 

Док-во $ \frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)$ -сумма нормальный распределений нормальное распределение 

$ E[\frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)] =\frac{\sqrt{n}}{\sigma}(E[\frac{1}{n}\sum^n_{i=1}(X_i)]-\mu_0) = \frac{\sqrt{n}}{\sigma}(\mu_0-\mu_0) = 0 $ 

$Var(\frac{\sqrt{n}}{\sigma}(\bar{X}-\mu_0)) = \frac{n}{\sigma^2}Var(\frac{1}{n}\sum^n_{i=1}X_i - \mu_0) =\frac{n}{\sigma^2} \frac{\sum^n_{i=1}X_i}{n^2} = 1 $ (в силу независимости)   

2. $ P(\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n} \in K_\alpha) = \alpha $  

$ P(\left\lvert\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}\right\rvert < Z_{\frac{\alpha}{2}}) = P_{H0}(Z> Z_{\frac{\alpha}{2}}) + P_{H0}(Z < -Z_{\frac{\alpha}{2}}) = \frac{\alpha}{2} + 1  - P_{H0}(Z>Z_{1-\frac{\alpha}{2}}) = \frac{\alpha}{2} + 1  - 1 + \frac{\alpha}{2} = \alpha$   

3) $Pvalue = 2\min(P(Z>Z_{набл},P(Z>Z_{набл})) = 2\min(1-P(Z \leq Z_{набл}), P(Z<Z_{набл})) = 2min(\frac{1}{2}-\Phi_0(\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}), \Phi_0(\frac{\bar{X}-\mu_0}{\sigma}\sqrt{n}) $

    """))

def solve_another_strange_number_8():
    display(Markdown(r"""
1) Рассмотрим статистику $T(X_1,...,X_n) = T = \frac{\bar X - \mu_0}{S}\sqrt{n}$, где $S=\sqrt{S^2}, S^2=\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar X)^2$

Тогда:

$
k_{\alpha} = \{\vec{X} \in \mathbb R^n ||T(X_1,...,X_n)|>t_{\alpha}(n-1) \}, \text{ где } t_{\alpha} - \text{ процентная точка распределения Стьюдента с } n-1 \text{ степенью свободы. }
$ 


2) $\frac{\bar X - \mu_0}{S}\sqrt{n} \sim T(n-1)$ - распределение стьюдента, если $H_0$ - верна.

Док-во:

$
\frac{\bar X - \mu_0}{S}\sqrt{n} = \frac{\frac{\bar X - \mu_0}{\sigma}\sqrt{n}}{\frac{\sqrt{S^2}}{\sigma}} = \frac{\frac{\bar X-\mu_0}{\sigma}}{\sqrt{\frac{(n-1)S^2}{\sigma}}\frac{1}{n-1}} = \{Z \sim Norm(0,1), \text{ Если H0 - верна } \} = \frac{Z}{\sqrt{\frac{\chi^2(n-1)}{n-1}}} =^{def} T\sim T(n-1)
$  


$k_{\alpha} = \{|T(X_1,...,X_n)| > t_{\alpha}(n-1) \}$

Док-во: Если Н0 верна, то $\frac{\bar X - \mu_0}{\sigma}\sqrt{n}\sim T(n-1)$  

$
\mathbb P\left(T(X_1,...,X_n) \in k_{\alpha} \right) = \mathbb P\left(\frac{\bar X - \mu_0}{\sigma}\sqrt{n} > t_{\alpha}(n-1) \right) = \mathbb P\left(T > t_{\alpha}(n-1) \right) =  \alpha
$ 


3)  $Pvalue = P(T(X_1,...,X_n)>t_{набл}) = P(\frac{\bar X - \mu_0}{S}\sqrt{n} > \frac{\bar X - \mu_0}{\sigma}\sqrt{n}) = \{ \frac{\bar X - \mu_0}{S}\sqrt{n} \sim T(n-1)\} = P(T > \frac{\bar X - \mu_0}{S}\sqrt{n}) = 1 - F_{t(n-1)}(\frac{\bar X - \mu_0}{S}\sqrt{n})  $ 
    """))

def solve_another_strange_number_9():
    display(Markdown(r"""
1) Рассмотрим статистику $T(X_1,...,X_n) = T = \frac{\bar X-\mu_0}{S}\sqrt{n}$

где $S = \sqrt{S^2}, S^2 = \frac{1}{n-1}\sum^n_{i=1}(X_i-\bar{X})^2$

Тогда $k_{\alpha}=\{\vec{X} \in \mathbb R^n | T(X_1,...,X_n) < t_{1-\alpha}(n-1) \}$, где $t_{\alpha}$ - процентная точка распределения стьюдента с n-1 степенью свободы

2) $\frac{\bar X - \mu_0}{S}\sqrt{n} \sim T(n-1)$ - распределение стьюдента, если $H_0$ - верна.

Док-во:

$$
\frac{\bar X - \mu_0}{S}\sqrt{n} = \frac{\frac{\bar X - \mu_0}{\sigma}\sqrt{n}}{\frac{\sqrt{S^2}}{\sigma}} = \frac{\frac{\bar X-\mu_0}{\sigma}}{\sqrt{\frac{(n-1)S^2}{\sigma}}\frac{1}{n-1}} = \{Z \sim Norm(0,1), \text{ Если H0 - верна } \} = \frac{Z}{\sqrt{\frac{\chi^2(n-1)}{n-1}}} =^{def} T\sim T(n-1)
$$

$k_{\alpha} = \{T(X_1,...,X_n)<t_{1-\alpha}(n-1) \}$

Док-во: Если H0 верна, то $\frac{\bar X - \mu_0}{\sigma}\sqrt{n}\sim T(n-1)$

$$
\mathbb P\left(T(X_1,...,X_n) \in k_{\alpha} \right) = \mathbb P \left(\frac{\bar X - \mu_0}{\sigma}\sqrt{n} < t_{1-\alpha}(n-1) \right) = \mathbb P\left(T<t_{1-\alpha}(n-1) \right) = 1 - \mathbb P\left(T>t_{1-\alpha}(n+1) \right) = 1-1+\alpha=\alpha
$$

3) $Pvalue = \mathbb P \left(T(X_1,...,X_n) < t_{набл} \right) = \mathbb P\left(\frac{\bar X-\mu_0}{S}\sqrt{n}<\frac{\bar X - \mu_0}{\sigma}\sqrt{n} \right) = \mathbb P(T<\frac{\bar X-\mu_0}{S}\sqrt{n}) = \mathbb F_{t(n-1)}(\frac{\bar X-\mu_0}{S}\sqrt{n})$
    """))

def solve_another_strange_number_10():
    display(Markdown(r"""
1) Рассмотрим статистику $T(X_1,...,X_n) = T = \frac{\bar X - \mu_0}{S}\sqrt{n}$, где $S=\sqrt{S^2}, S^2=\frac{1}{n-1}\sum^n_{i=1}(X_i-\bar X)^2$

Тогда:

$
k_{\alpha} = \{\vec{X} \in \mathbb R^n ||T(X_1,...,X_n)|>t_{\frac{\alpha}{2}}(n-1) \}, \text{ где } t_{\alpha} - \text{ процентная точка распределения Стьюдента с } n-1 \text{ степенью свободы. }
$

2) $\frac{\bar X - \mu_0}{S}\sqrt{n} \sim T(n-1)$ - распределение стьюдента, если $H_0$ - верна.

Док-во:

$
\frac{\bar X - \mu_0}{S}\sqrt{n} = \frac{\frac{\bar X - \mu_0}{\sigma}\sqrt{n}}{\frac{\sqrt{S^2}}{\sigma}} = \frac{\frac{\bar X-\mu_0}{\sigma}}{\sqrt{\frac{(n-1)S^2}{\sigma}}\frac{1}{n-1}} = \{Z \sim Norm(0,1), \text{ Если H0 - верна } \} = \frac{Z}{\sqrt{\frac{\chi^2(n-1)}{n-1}}} =^{def} T\sim T(n-1)
$

$k_{\alpha} = \{|T(X_1,...,X_n)| > t_{\frac{\alpha}{2}}(n-1) \}$

Док-во: Если Н0 верна, то $\frac{\bar X - \mu_0}{\sigma}\sqrt{n}\sim T(n-1)$

$
\mathbb P_{H_0}\left(T(X_1,...,X_n) \in k_{\alpha} \right) = \mathbb P_{H_0}\left(|\frac{\bar X - \mu_0}{\sigma}\sqrt{n}| > t_{\frac{\alpha}{2}}(n-1) \right) = \mathbb P\left(|T| > t_{\frac{\alpha}{2}}(n-1) \right) = \mathbb P\left(T<t_{1-\frac{\alpha}{2}}(n-1) \right) + \mathbb P\left(T > t_{\frac{\alpha}{2}}(n-1) \right) = \frac{\alpha}{2} + \frac{\alpha}{2} = \alpha
$

3) $Pvalue = 2min \{\mathbb P\left(T>t_{набл} \right); \mathbb P\left(T < t_{набл} \right) \} = \{\text{распределение Стьюдента имеем четкую плотность, тогда:} \} = 2min \{\mathbb P\left(T>|t_{набл}| \right);\mathbb P \left(T < -|t_{набл}| \right) \} = 2\mathbb P\left(T < -|t_{набл}| \right) = 2\mathbb F_{T(n-1)}(-|t_{набл}|)$ 


    """))

def solve_another_strange_number_11():
    display(Markdown(r"""
1) Рассмотрим статистику $\chi^2_0 = \frac{1}{\sigma^2_0} \sum^n_{k=1}(X_k-\mu)^2$

$
k_{\alpha} = \{\vec{X} \in \mathbb R | \chi^2_0>\chi^2_{\alpha}(n)\}, \text{ где } \chi^2_{\alpha}(n) - \text{ процентная точка уровня } \alpha \text{ для } \chi^2 \sim \chi^2(n)
$

2) Если $H_0$ - верна, то $\chi^2_0=\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2 \sim \chi^2(n)$

Док-во:

$\chi^2_0=\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2 = \sum^n_{k=1}(\frac{X_k-\mu}{\sigma})^2 = \sum^n_{k=1}\mathcal Z^2_k =^{def} \chi^2(n)$

$
\mathbb P_{H_0}\left(T(X_1,...,X_n \in k_{\alpha}) \right) = \alpha
$

$
\mathbb P_{H_0}\left(\frac{1}{\sigma^2_0} \sum^n_{k=1}(X_k-\mu)^2 > \chi^2_{\alpha}(n) \right) = \mathbb P_{H_0}\left(\chi^2(n) > \chi^2_{\alpha}(n) \right) =^{def} = \alpha
$

3)$Pvalue = \mathbb P_{H_0}\left(T(X_1,...,X_n) > \chi^2_{набл} \right) = \mathbb P_{H_0}\left(\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2>\chi^2_{набл} \right) = 1-\mathbb F_{\chi^2(n)}\left(\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2\right)$


    """))

def solve_another_strange_number_12():
    display(Markdown(r"""

1) Рассмотрим статистику $\chi^2_0 = \frac{1}{\sigma^2_0} \sum^n_{k=1}(X_k-\mu)^2$

$
k_{\alpha} = \{\vec{X} \in \mathbb R | 0<\chi^2_0<\chi^2_{1-\alpha}(n)\}, \text{ где } \chi^2_{1-\alpha}(n) - \text{ процентная точка уровня } 1-\alpha \text{ для } \chi^2 \sim \chi^2(n)
$

2) Если $H_0$ - верна, то $\chi^2_0=\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2 \sim \chi^2(n)$

Док-во:

$\chi^2_0=\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2 = \sum^n_{k=1}(\frac{X_k-\mu}{\sigma})^2 = \sum^n_{k=1}\mathcal Z^2_k =^{def} \chi^2(n)$

$
\mathbb P_{H_0}\left(T(X_1,...,X_n \in k_{\alpha}) \right) = \alpha
$

$
\mathbb P_{H_0}\left(0 < \frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2 <\chi^2_{1-\alpha}(n) \right) = \mathbb P_{H_0}\left(0<\chi^2(n)<\chi^2_{1-\alpha}(n) \right) = \mathbb P\left(\chi^2(n)>0 \right) - \mathbb P\left(\chi^2(n)>\chi^2_{1-\alpha}(n) \right) = 1-1+\alpha - \alpha
$

3)$Pvalue = \mathbb P_{H_0}\left(T(X_1,...,X_n) < \chi^2_{набл} \right) = \mathbb P_{H_0}\left(\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2<\chi^2_{набл} \right) = \mathbb F_{\chi^2(n)}\left(\frac{1}{\sigma^2_0}\sum^n_{k=1}(X_k-\mu)^2 \right)$
    """))
