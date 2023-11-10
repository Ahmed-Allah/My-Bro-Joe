# دى بتطبع الحاجه print أسمها  functionأول
print("3la Allah")
print("i love python")
# objectجميع البيانات فى لغة بايثون عباره عن
# دى بتطلع نوع البياناتtype فى حاجه أسمها

# وده للأرقام الصحيحه الى مفيهاش كسورintger  أول نوع أسمه
print(type(10))  # int => Intger
print(type(100))  # int => Intger
print(type(-50))  # int => Intger
# ---------------------------------------------------

# وده للأرقام الى فيها كسورfloatثانى نوع أسمه
print(type(100.9))  # float => Floating Point Number
print(type(-100.9))  # float => Floating Point Number

# ---------------------------------------------------

# وده لكل النصوصstring  النوع الثالث أسمه
print(type("Hello"))  # str => String


# ---------------------------------------------------

# دهالى هو المصفوفهlistفى نوع الرابع أسمه
print(type([1, 2, 3]))  # List => lis

# ---------------------------------------------------

#  ده زى الى فوقيها بس الفرقان دى جوا قوسينtupleفى نوع خامس أسمه

print(type((1, 2, 3)))  # tuple => tuple


# ---------------------------------------------------

# ده عباره عن قاموس وبيبقى مثلا الكلمه ومعنهاdict فى نوع سادس أسمه

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => dictionary

# ---------------------------------------------------

# ده الى هو القيمه المنطقيهBooleanفى نوع ثانى أسمه

print(type(2 == 2))  # bool => Boolean

# بتكتب أسمها بس و القيمه وخلاصvaribale عشان تعمل

varibale = "This Is a Varibale"
print(varibale)

# this for know me what is the keywords use
help("keywords")

# ده لو عشان تعمل اكتر من متغير بأكتر من قيمه فى وقت واحد
c, b, f = 1, 2, 3

# دى بتشيل أخر الحاجه الى قبلها  Back Spaceفى حاجه أسمها
print("Hello\bworld")

#  ودى لما تضيف حاجه تبع السطر الأول مع الثانى بتدمجهمBack slashفى حاجه أسمها
print(" Hello \
I love \
python")
# دى بتعمل سطر جديد\nفى حاجه أٍسمها
print("hello\nworld")

# دى بتبدل عدد الاحرف الى على اليمين بتجيبه فى الشمال\r فى حاجه أٍسمها
print("123456\rabcde")
#  دى بتعمل مسافه طويله بين الكلام\tفى حاجه اسمها
print("Hello\tWOrld")
#  لكلام HEX دى بتحول الكلام بتاع ال  \x فى حاجه أسمها
print("\x4f")

msg = "I love"
lang = "python"

# + طبعا عشان ترتبط بين متغيرين بتعمل علامة
print(msg + lang)
#  دى عشان تعمل بينهم مسافه
print(msg + " " + lang)

# دى عشان لو عايز تميز حاجه معينه
mystringone = "this in `test`"

print(mystringone)

# multible codes دى بتعمل
strinng = """this
is
multiple code"""

print(strinng)


test = "I Love Paython"
# معينه Itemدى عشان تجيب
print(test[0])
# دى بتحدد منها برضو بس عكس البى فات وبتبداء من اليمين
print(test[-2])

# دى لو أنت عايز تاخد جزء معين من لاكلام بس فى النهايه بتذود واحد
print(test[0:4])

# دى بقى بتخليك تاخد خطوات
print(test[::2])

# دى بتعد العناصر الى جوا  lenفى حاجه أسمها
print(len(test))

a = "        I love Python     "


# دى بتشيل المسافات على اليمين و الشمالstrip قى حاجه أسمها
print(a.strip())
# دى بتشيل المسافات على اليمينrstrip وفى حاجه أسمها
print(a.rstrip())
# دى بتشيل المسافات الى على الشمالlstrip وفى حاجه أسمها
print(a.lstrip())


a = "##@##I love Python#@####"

# لو عايز تشيل حاجه معينه بتكتبها جوا القوص
print(a.strip("#@"))
print(a.rstrip("#@"))
print(a.lstrip("#@"))


b = "I love 2d Graphics and 3g Technology and python"
#  دى بتخلى الأحرف الى فى الأول كبيره title فى حاجه أسمها
print(b.title())
# دى زي الى فوق بس دى مش بتشتغل فى الارقام وكده
print(b.capitalize())

bb, vv, aa = "1", "11", "111"

#  دى بتضيف صفر قبل الإرقامzfill فى حاجه أسمها
print(bb.zfill(3))
print(vv.zfill(3))
print(aa.zfill(3))

g = "Ahmed"
# دى بتخلى كل الحروف كبيرهupper فى حاجه أسمها
print(g.upper())
# دى بتخلى كل الحروف صغيره
print(g.lower())

ilove = "I Love Python And PHP"
# list دى بتقسم الحجات ويجعها فى  split فى حاجه أسمها
print(ilove.split())

ilove1 = "I-Love-Python-And-PHP"
# طبعا لو انت عايز تقطع من جزء معين بتعمل كده
print(ilove1.split("-"))

ilove2 = "I-Love-Python-And-PHP"
# دى هنا بيكون ليها نهايه وبدايه بتحدد الى عايزها وبعدها بالقيمه الى بتحددها والباقى لوحدهم
print(ilove2.split("-", 2))

ilove2 = "I-Love-Python-And-PHP"
# ده زى الى فوق بس بتبدأ من العكس
print(ilove2.rsplit("-", 2))

aasa = "Ahmed"
# دى حاجه بتحط أى حاجه قبل الكلام وبعدهcenter فى حاجه أسمها
print(aasa.center(15, "#"))

q = "Ahmed Mido"
# دى بتشوف الحاجه الى أنت كاتبها وبيشوفهالكموجوده كام مره countفى حاجه أسمها
print(q.count("Ahmed"))
# دى بتشوفها من قيمه لقيمه ثانيه
print(q.count("Ahmed", 1, 5))

zx = "I Love Python"
# دى بتحول الحروف الكبيره لصغيره و العكسswapcase فى حاجه أسمها
print(zx.swapcase())
# دى بتسأله إذا كان هيبداء بحاجه و لا لا  startswithفى حاجه أسمها
print(zx.startswith("I"))
print(zx.startswith("S"))
print(zx.startswith("P", 7, 12))
# دى عكس الى فوق
print(zx.endswith("n"))
# دى بتبحث عن حاجه كوا الجمله وليها بدايه و نهايه او من غير بس دى بتعمل ايرور لو ملقتش حاجه index فى حاجه أسمها
print(aasa.index("m"))
print(aasa.index("m", 0, 5))
# print(aasa.index("m", 5 , 5))

# زيها زى الى فوق بس دى مبتعملش ايرورfind  فى حاجه اسمها
print(zx.find("L", 0, 5))
print(zx.find("L"))
print(zx.find("L", 5, 5))

# دى بتضيف حجات قبل الكلمه من الشمال rjust فى حاجه أسمها
a_1 = "Ahmed"
print(a_1.rjust(10))
print(a_1.rjust(10, "#"))
# دى بتضيف حجات قبل الكلمه من اليمينljust فى حاجه أسمها
print(a_1.ljust(10))
print(a_1.ljust(10, "#"))

e1 = """first line
Second Line
Third line"""

# list دى بتحطلك الكلمات الى فى سطور جوا  splitlinesفى حاجه أسمها
print(e1.splitlines())

f1 = "First Line \nSecondLine\nThird Line"
print(f1.splitlines())

g1 = "Hello\tWorld\tI\tLove\tPython"
# دى بتتحكم فى عدت التابات الموجوده expandtabs فى حاجه أسمها
print(g1.expandtabs(2))

one1 = "I Love Python And 3G"
# ولا لاtitle دى من خلالها بتعرف إذا كان ده  istitle فى حاجه أسمها
print(one1.istitle())

two2 = ""
# دى بتتأكد منها إذا كانت فيها مسافه ولا لا  isspace قى حاجه أسمها
print(two2.isspace())
# دى بتتأكد منها إذا كان كل الحروف صغيره islower فى حاجه أسمها
print(one1.islower())
three3 = "Ahmed_Mido"
# دى بتتأكد منها إذا كان ينفع يبقى متغير ولا لأisidentifier فى حاجه أسمها
print(three3.isidentifier())

Four4 = "AAAAaaaa"
# ده بيشوف إذا كان ترتيب الكلمه ترتيب أبجدى ولا لأisalpha فى حاجه أسمها
print(Four4.isalpha())

five5 = "AAAAaaaa5454"
# دى بتشوف إذا كان فى أرقام ولا لا isalnum فى حاجه أسمها
print(Four4.isalnum())

amm = "Hello One Two One One"
#  دى بتبدل الحجات replaceفىحاجه أسمها
print(amm.replace("One", "1"))
print(amm.replace("One", "1", 2))


mylist = ["Osama", "mohamed", "Ahmed"]
# دى بتضيف حاجه وسطهمjoin فى حاجه أسمها
print("-".join(mylist))

# ------------------------
# -- Strings Formatting --
# ------------------------

name12 = "Osama"
age12 = 36
rank12 = 10

print("My Name Is : " + name12)
# print("My Name Is : " + name12 + "and my Age Is :" + age12)  # Type Error

# % فى أخر الجمله وبعديها علامة %s دى عشان تحط متغير مع كلمه عادى ودى بتستخدم عن طريق انك بتحط place holder فى حاجه أسمها
print("My Name Is %s" % name12)
print("My Name is: %s and My Age is: %d" % (name12, age12))
print("My Name is: %s and My Age is: %d and My Rank is: %f" %
      (name12, age12, rank12))

# %s => String
# %d => Number
# %f => Float

n = "Ahmed"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10

print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
# حط عدد الأصفار الى هيتحط بعد الرقم F لو عايز تتحكم فى عدد الأصفار فبل حرف ال
print("My Number is: %.2f" % myNumber)

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
# عدد الأحرف الى ا،ت عايزها S لو أنت عايز حاجه معينه من نص بتعمل قبل ال
print("Message is %.13s" % myLongString)

# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------

name77 = "Osama"
age77 = 36
rank77 = 10

# Format دى الطريقه الجديده لل
print("My Name is: {}".format(name77))
print("My Name is: {}".format("Ahmed"))

print("My Name is: {} My Age: {}".format(name77, age77))
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(
    name77, age77, rank77))

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))


# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
# هنا لما يكون فى أرقام كتيره وعايز تقسم بيها بتححد العلامه وتعملها كده
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney))

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
# ده هنا عشان تغير المكان براحتك
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

myName = "Osama"
myAge = 36

print("My Name is : {myName} and My Age is : {myAge}")
# format در برضو طريقه جديده عشان تعمل
print(f"My Name is : {myName} and My Age is : {myAge}")
