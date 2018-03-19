from selenium import webdriver
from keysProcess import keyGenerator
from random import Random

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path='C:\Gaming\chromedriver.exe',options=chromeOptions)

username = 161002516
password = 161002516

driver.get(url="http://202.204.121.159/")

driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_class_name("newlogintable_third_button").click()

driver.get('http://202.204.121.159/book/index.php?BookID=184&ClassID=9089&Quiz=N')
driver.get('http://202.204.121.159/book/book184/app_index.php?unit=1')

a = keyGenerator()
list = a.getKeys()

percent = 80
ran = Random()

for (i, j) in list:
    form_data = ''
    form_data +='ItemID=' + i
    for key in j.split('^'):
        if ran.random() > percent/100:
            key = ''
        form_data+='&answer[]=' + key
    result = driver.execute_script('''
    var done = false;
    var score = 0;
    $.ajaxSetup({
                async : false
            });

    $.post('postDrag.php',arguments[0] , function (data) {
        // console.log('------- '+count + ' ------- ');
        // console.log(' : ' + data);
        var question = JSON.parse(data);
        if(question.key!==''){
            console.log(question.myPercentScore);
            score =  question.myPercentScore;
            done = true;
        }
    }).error(function () {
        console.log('error');
        done = true;
        return 'error';
    })
    while(!done){
        
    }
    return score;
    ''',form_data)
    print(result)