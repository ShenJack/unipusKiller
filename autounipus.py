from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')

username = 161002516
password = 161002516

driver.get(url="http://202.204.121.159/")

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("newlogintable_third_button").click()

driver.get('http://202.204.121.159/book/index.php?BookID=184&ClassID=9089&Quiz=N')
driver.get('http://202.204.121.159/book/book184/app_index.php?unit=1')

my_script = open("answer.js", encoding='utf-8').read()
# addIn = "var keyScore = %s; \n" % (80 / 100)

for j in range(0,180):
    result = driver.execute_script('''
    var count = 1;
    var content = '';
    $.post('postDrag.php', {
        ItemID: arguments[0],
    }, function (data) {
        var question = JSON.parse(data);
        if(question.key!==''){
            return ('------- '+count + ' ------- ' + ' : ' + data);
            count++;
        }else{
            return ('none error');
        }
    }).error(function () {
        return ('error');
    })
''',j)
    print(result)