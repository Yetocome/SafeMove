    function showUpload(){
      var div = document.getElementById("container");
      div.style.display = "block";
    }
    
    function hideUpload(){
      var div = document.getElementById("container");
      div.style.display = "none";
    }

    window.onload = function(){
      var div = document.getElementById("container");
      div.style.display = "none";
    };

     function isSupportCanvas() {
        var elem = document.createElement('canvas');
        return !!(elem.getContext && elem.getContext('2d'));
    }

    function submitAlert() {
      var obj = document.getElementById("detail");
      if (obj.value != "") {
        alert('上传成功!感谢您的贡献！');
      }
    }