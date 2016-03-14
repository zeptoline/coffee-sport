$(function(){
  var min = 0;
  var max = 100;
  function init_button() {
    min = 0;
    max = 100;
    $('#dec').prop('disabled', true);
    $('#inc').prop('disabled', false);
  }
  init_button();
  function incr() {
    $('#dec').prop('disabled', false);
    min += 100;
    max += 100;
  }
  function decr() {
    min -= 100;
    max -= 100;
    if(min == 0)
      $('#dec').prop('disabled', true);
  }


  function create_table(fichier) {
    $.ajax({
      // chargement du fichier externe
      url      : "http://172.21.65.162:8080/view/"+fichier,
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {

        var result = [];
        var table = [];
        var html = "";
        var entete = [];
        for (var i in data[0])
        entete.push(i);

        for(var i in data){
          for(var j in data[i]){
            result.push([data[i][j]]);
          }
          table.push(result);
          result = [];
        }

        html+= "<thead><tr>"
        html += "<th>indice</th>";
        $.each(entete, function(i) {
          html += "<th>"+entete[i]+"</th>";
        });

        html+= "</tr></thead>"

        $.each(table, function(i) {
          if(i < max && i >= min){
            html += "<tr>";
            html += "<td>"+(i+1)+"</td>";
            $.each(table[i], function(j) {
              html += "<td>"+table[i][j]+"</td>";
            });
            html += "</tr>";
          }
        });

        $("#data").html(html);
      }
    });
  }



  $("#submit_ins").on("click", function() {
    init_button();
    create_table("installations");
  });
  $("#submit_act").on("click", function() {
    init_button();
    create_table("activites");
  });
  $("#submit_eqpt").on("click", function() {
    init_button();
    create_table("equipements");
  });

  $("#inc").on("click", function() {
    incr();
    create_table("equipements");
  });
  $("#dec").on("click", function() {
    decr();
    create_table("equipements");
  });

});
