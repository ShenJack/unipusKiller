'use strict';
var count = 1;
var content = '';
var keys = [];
var ids = [];
$.ajaxSetup({
            async : false
        });

for (var i = 1; i < 200;i++) {
    $.post('postDrag.php', {
        ItemID: i
    }, function (data) {
        // console.log('------- '+count + ' ------- ');
        // console.log(' : ' + data);
        var question = JSON.parse(data);
        if(question.key!==''){
            keys.push(question.key);
            ids.push(i);
        }
    }).error(function () {
        console.log('error');
    })
}

console.log(keys.join('*'));
console.log(ids.join('*'));

var funDownload = function (content, filename) {
    // 创建隐藏的可下载链接
    var eleLink = document.createElement('a');
    eleLink.download = filename;
    eleLink.style.display = 'none';
    // 字符内容转变成blob地址
    var blob = new Blob([content]);
    eleLink.href = URL.createObjectURL(blob);
    // 触发点击
    document.body.appendChild(eleLink);
    eleLink.click();
    // 然后移除
    document.body.removeChild(eleLink);
};

// noinspection JSAnnotator
var arguments = ['7','Exciting jobs,right under 30 your diet and your nutrition making a lot of money passionate about windsurfing looking at the wind going to prepare that magical balance not to be afraid'];

keys = arguments[1].split(' ');


$.post('postDrag.php', {
        ItemID: arguments[0]
    }, function (data) {
        // console.log('------- '+count + ' ------- ');
        // console.log(' : ' + data);
        var question = JSON.parse(data);
        if(question.key!==''){
            keys.push(question.key);
            ids.push(i);
        }
    }).error(function () {
        console.log('error');
    });
$.post('postDrag.php', , function (data) {
        // console.log('------- '+count + ' ------- ');
        // console.log(' : ' + data);
        var question = JSON.parse(data);
        if(question.key!==''){
            console.log(question.myPercentScore);
            return question.myPercentScore;
        }
    }).error(function () {
        console.log('error');
        return 'error';
    });