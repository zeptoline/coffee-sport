<?php
header("Access-Control-Allow-Origin: *");
?>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <title>jQuery.getJSON demo</title>
  <style>
  img {
    height: 100px;
    float: left;
  }
  </style>
  <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
</head>
<body>



<script>
(function() {
  var installations = "http://localhost:8080/view/installations";
  $.getJSON(installations, function(result){
        $.each(result, function(i, field){
            $("div").append(field + " ");
        });
    });
})();
</script>

</body>
</html>
