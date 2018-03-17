'use strict';
var pages = new Map();
pages.add();
var count = 1;
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
    })
}