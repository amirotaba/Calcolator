from flask import Flask, render_template, request

show = []
num = []
num1 = 0

app = Flask(__name__, template_folder='templates')


# functions
def make_int():
    global item, type
    strings = [str(integer) for integer in num[0: len(num) - 1]]
    a_string = "".join(strings)
    for obj in a_string:
        if obj == ".":
            type = "flt"
    if type == "flt":
        item = float(a_string)
    else:
        item = int(a_string)


def seprate():
    global func, num, num1, show
    make_int()
    num1 = item
    func = num[-1]
    num = []


def get_result():
    global num1, num, result, num2
    make_int()
    num2 = item
    if func == "+":
        result = num2 + num1
    elif func == "-":
        result = num1 - num2
    elif func == "×":
        result = num2 * num1
    elif func == "÷":
        result = num1 / num2


def display(number):
    global show, num, dis
    for obj in show:
        if obj == "=":
            clean()
    show.append(number)
    strings = [str(integer) for integer in num[0: len(num)]]
    dis = "".join(strings)


def clean():
    global num, num1, num2, dis, func
    num = []
    num1 = None
    num2 = None
    dis = " "
    func = None


@app.route('/', methods=["POST", "GET"])
def get_number():
    if request.method == "POST":
        global num1
        global num
        if request.form.get("1"):
            num.append(1)
            display(1)
        elif request.form.get("2"):
            num.append(2)
            display(2)
        elif request.form.get("3"):
            num.append(3)
            display(3)
        elif request.form.get("4"):
            num.append(4)
            display(4)
        elif request.form.get("5"):
            num.append(5)
            display(5)
        elif request.form.get("6"):
            num.append(6)
            display(6)
        elif request.form.get("7"):
            num.append(7)
            display(7)
        elif request.form.get("8"):
            num.append(8)
            display(8)
        elif request.form.get("9"):
            num.append(9)
            display(9)
        elif request.form.get("0"):
            num.append(0)
            display(0)
        elif request.form.get("."):
            num.append(".")
            display(".")
        elif request.form.get("+"):
            num.append("+")
            seprate()
            return render_template("cal_func.html", num1=num1, func=func, dis=dis)
        elif request.form.get("-"):
            num.append("-")
            seprate()
            return render_template("cal_func.html", num1=num1, func=func)
        elif request.form.get("*"):
            num.append("×")
            seprate()
            return render_template("cal_func.html", num1=num1, func=func)
        elif request.form.get("/"):
            num.append("÷")
            seprate()
            return render_template("cal_func.html", num1=num1, func=func)
        elif request.form.get("="):
            num.append("=")
            get_result()
            return render_template("cal_res.html", num1=num1, func=func, dis=dis, result=result)
        elif request.form.get("C"):
            clean()
            return render_template("cal.html", dis=dis) 
        if "func" in globals() and func != None:
            return render_template("cal_mid.html", num1=num1, func=func, dis=dis)
        else:
            return render_template("cal.html", dis=dis)
    elif request.method == 'GET':
        return render_template("cal.html", show=show)


if __name__ == '__main__':
    app.run()
