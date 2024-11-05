from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/q1', methods=['GET', 'POST'])
def q1():
    result = None
    if request.method == 'POST':
        weight = int(request.form['weight'])
        if weight % 2 == 0 and weight > 2:
            result = "YES"
        else:
            result = "NO"
    return render_template('q1.html', result=result)

@app.route('/q2', methods=['GET', 'POST'])
def q2():
    result = 0
    if request.method == 'POST':
        n = int(request.form['problems_count'])
        for i in range(n):
            opinion = request.form.getlist(f'opinion{i}')
            opinion = list(map(int, opinion))
            if sum(opinion) >= 2:
                result += 1
    return render_template('q2.html', result=result)

@app.route('/q3', methods=['GET', 'POST'])
def q3():
    average_caffeine = None
    if request.method == 'POST':
        n = int(request.form['drinks_count'])
        caffeine_levels = list(map(int, request.form.getlist('caffeine_levels')))
        average_caffeine = sum(caffeine_levels) / n
    return render_template('q3.html', result=average_caffeine)

@app.route('/q4', methods=['GET', 'POST'])
def q4():
    result = []
    if request.method == 'POST':
        t = int(request.form['test_cases_count'])
        for i in range(t):
            a = int(request.form[f'a{i}'])
            b = int(request.form[f'b{i}'])
            c = int(request.form[f'c{i}'])
            if a + b == c or a + c == b or b + c == a:
                result.append("YES")
            else:
                result.append("NO")
    return render_template('q4.html', result="\n".join(result))

@app.route('/q5', methods=['GET', 'POST'])
def q5():
    min_cost = None
    if request.method == 'POST':
        n = int(request.form['n'])
        a = int(request.form['a'])
        b = int(request.form['b'])

        pairs = n // 2
        remainder = n % 2
        min_cost = (pairs * b) + (remainder * a)
        
        if n * a < min_cost:
            min_cost = n * a

    return render_template('q5.html', result=min_cost)

@app.route('/q6', methods=['GET', 'POST'])
def q6():
    result = None
    if request.method == 'POST':
        n = int(request.form['n'])
        p = int(request.form['p'])
        majeds_courses = list(map(int, request.form['majeds_courses'].split())) if p > 0 else []
        q = int(request.form['q'])
        fahds_courses = list(map(int, request.form['fahds_courses'].split())) if q > 0 else []

        combined_courses = set(majeds_courses) | set(fahds_courses)
        
        if len(combined_courses) == n and all(course in combined_courses for course in range(1, n + 1)):
            result = "I become the guy."
        else:
            result = "Oh, my keyboard!"

    return render_template('q6.html', result=result)

@app.route('/q7', methods=['GET', 'POST'])
def q7():
    result = None
    if request.method == 'POST':
        n = int(request.form['n'])
        k = int(request.form['k'])

        not_divisible_count = (k - 1) + (k - 1) // (n - 1)
        kth_number = not_divisible_count + 1 if (k + not_divisible_count) % n != 0 else not_divisible_count + 2

        result = kth_number

    return render_template('q7.html', result=result)

