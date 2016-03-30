$(function(){
  var min = 0;
  var max = 100;
  $(".donnee").css({"display":"none"});

  function init_button(bt) {
    min = 0;
    max = 100;
    $('#dec_'+bt).prop('disabled', true);
    $('#inc_'+bt).prop('disabled', false);
  }
  function incr(bt) {
    $('#dec_'+bt).prop('disabled', false);
    min += 100;
    max += 100;
  }
  function decrbt() {
    min -= 100;
    max -= 100;
    if(min == 0)
    $('#dec_'+bt).prop('disabled', true);
  }


  function create_table(fichier) {
    $.ajax({
      // chargement du fichier externe
      url : "http://172.21.65.184:8080/view/"+fichier,
      // data     : {
      //
      // },
      // Passage des données au fichier externe
      cache    : false,
      dataType : "json",
      error    : function(request, error) { // Info Debuggage si erreur
        alert("Erreur : responseText: "+request.responseText);
      },
      success  : function(data) {

        var target= $("#"+fichier);

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

        $("#data_"+fichier).html(html);
      }
    });
  }


  // INSTALLATIONS //
  $("#submit_ins").on("click", function() {
    init_button("ins");
    $(".donnee").css({"display":"none"});
    $("#installations").css({"display":"block"});
    $('html, body').animate({
        scrollTop: $("#installations").offset().top
    }, 1000);
    create_table("installations");
  });
  $("#inc_ins").on("click", function() {
    incr("ins");
    create_table("installations");
  });
  $("#dec_ins").on("click", function() {
    decr("ins");
    create_table("installations");
  });

  // ACTIVITES //
  $("#submit_act").on("click", function() {
    init_button("act");
    $(".donnee").css({"display":"none"});
    $("#activites").css({"display":"block"});
    $('html, body').animate({
        scrollTop: $("#activites").offset().top
    }, 1000);
    create_table("activites");
  });
  $("#inc_act").on("click", function() {
    incr("act");
    create_table("activites");
  });
  $("#dec_act").on("click", function() {
    decr("act");
    create_table("activites");
  });

  // EQUIPEMENTS //
  $("#submit_eqpt").on("click", function() {
    init_button("eqpt");
    $(".donnee").css({"display":"none"});
    $("#equipements").css({"display":"block"});
    $('html, body').animate({
        scrollTop: $("#equipements").offset().top
    }, 1000);
    create_table("equipements");


  });
  $("#inc_eqpt").on("click", function() {
    incr("eqpt");
    create_table("equipements");
  });
  $("#dec_eqpt").on("click", function() {
    decr("eqpt");
    create_table("equipements");
  });


  $(".showdiv").hide();
  $(".revealbutton").click(function() {
    if($(this).next().next().next().css('display') != 'none') {
      $(".showdiv").hide("slow");
    } else {
      $(".showdiv").hide("slow");
      $(this).next().next().next().show("slow");
    }

  });




});
