
// 监听select models 安排物种选择
$("#select_models").change(function () {
    let selected = $(this).children('option:selected').val();
    console.log(selected)
    target = document.getElementById("select_spieces");
    while (target.options.length) {
        target.remove(0);
    }
    Tools = ["CNCI", "CPC2", "lgc", "PLEK", "CPAT", "CPPred", "longdist", "PredLnc-GFStack", "LncADeep","DeepCPP"];
    for (i = 0; i < Tools.length; i++) {
        if (selected == Tools[i]) {
            // 局部刷新
            idx = i;
            $.get('/static/json/spieces.json', function (data) {
                for (let j in data) {
                    console.log(idx);
                    if (data[j].modelID == idx) {
                        console.log(j);
                        console.log(data[j].name);
                        $('#select_spieces').append("<option>" + data[j].name + "</option>");
                    }
                };
            });
        }
    }

});

function copy() {
    var copyTest = document.getElementById("uid").innerText;
    var inputTest = document.createElement('input');
    inputTest.value = copyTest;
    document.body.appendChild(inputTest);
    inputTest.select();
    document.execCommand("Copy");
    inputTest.className = 'oInput';
    inputTest.style.display = 'none';
    // $('#copyid').text('copy successed!');
    
    alert('复制成功');
}




// $("#showtaskid").hover(function(){
//     $("#copybtn").show();
// });


//  上传文件的函数
// function uploadData() {

//     model = $('#select_models option:selected').text();
//     if (model === "Select models") {
//         alert('请选择模型！');
//     }
//     else if (flexRadioDefault1.checked == true) {
//         // 粘贴框的文件
//         inputdata = textarea_data.value;
//         if (inputdata === "") {
//             alert('请粘贴数据！');
//         }
//     }
//     else if (flexRadioDefault2.checked == true) {

//         let files = $('#xFile').prop('files');
//         if (files.length === 0) {
//             alert('请选择文件！');
//         } else {
//             let reader = new FileReader();
//             reader.readAsText(files[0], "UTF-8");
//             reader.onload = function (evt) {
//                 let fileString = evt.target.result;
//                 outputframe.value = fileString;
//             }
//         }
//     }
//     else {
//         alert("请选择上传方式！")
//     }

//     outputframe.value = inputdata;
// }




// function downLoadResult() {
//     filename = document.getElementById("getid").value;
//     let filepath = '/home/xxr/lncRNAwebtool/predict_results'+filename
    
//     let blob = new Blob([content], {
//         type: "text/plain;charset=utf-8"
//     });

//     saveAs(blob, filename);
// }

