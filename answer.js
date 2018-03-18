'use strict';
var pages = new Map();
pages.add();
var count = 1;
var content = '';
for (var i = 1; i < 250;i++) {
    $.post('postDrag.php', {
        ItemID: i
    }, function (data) {
        // console.log('------- '+count + ' ------- ');
        // console.log(' : ' + data);
        var question = JSON.parse(data);
        if(question.key!==''){
            console.log('------- '+count + ' ------- ');
            console.log(' : ' + data);
            count++;
        }
    }).error(function () {
        console.log('error');
    })
}

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