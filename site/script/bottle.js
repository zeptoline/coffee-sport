$(function(){
  var ip = "http://188.166.171.162:8080";



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
  function decr(bt) {
    min -= 100;
    max -= 100;
    if(min == 0)
    $('#dec_'+bt).prop('disabled', true);
    $('#inc_'+bt).prop('disabled', false);
  }


  function create_table(fichier, nom_commune, data2, data3) {
    if(nom_commune == ""){
      nom_commune = null;
    }
    if(data2 == ""){
      data2 = null;
    }
    if(data3 == ""){
      data3 = null;
    }

    $.ajax({
      // chargement du fichier externe

      url      : ip+"/view/"+fichier+"/"+nom_commune+"/"+data2+"/"+data3,
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

        if(fichier == "activites"){
          var comm = -1;
          $("#data_activites thead tr th").each(function(index) {
            if($(this).text() == "nom commune") {
              comm = index;
            }
          });





          
        }
      }
    });
  }

  function clickActivite() {


    alert(comm);



  }

  // INSTALLATIONS //
  $("#submit_ins").on("click", function() {
    init_button("ins");
    $(".donnee").css({"display":"none"});
    $("#installations").css({"display":"block"});

    $('html, body').animate({
        scrollTop: $("#installations").offset().top
    }, 1000);

    create_table("installations", $("#installations_commune_ins").val(), $("#nom_usuel_install_ins").val(), null);
  });
  $("#inc_ins").on("click", function() {
    incr("ins");
    create_table("installations", $("#installations_commune_ins").val(), $("#nom_usuel_install_ins").val(), null);
  });
  $("#dec_ins").on("click", function() {
    decr("ins");
    create_table("installations", $("#installations_commune_ins").val(), $("#nom_usuel_install_ins").val(), null);
  });

  // ACTIVITES //
  $("#submit_act").on("click", function() {
    init_button("act");
    $(".donnee").css({"display":"none"});
    $("#activites").css({"display":"block"});
    $('html, body').animate({
        scrollTop: $("#activites").offset().top
    }, 1000);
    create_table("activites", $("#activites_commune_act").val(), $("#activite_libelle_act").val(), null);

    clickActivite();
  });
  $("#inc_act").on("click", function() {
    incr("act");
    create_table("activites", $("#activites_commune_act").val(), $("#activite_libelle_act").val(), null);
  });
  $("#dec_act").on("click", function() {
    decr("act");
    create_table("activites", $("#activites_commune_act").val(), $("#activite_libelle_act").val(), null);
  });

  // EQUIPEMENTS //
  $("#submit_eqpt").on("click", function() {
    init_button("eqpt");
    $(".donnee").css({"display":"none"});
    $("#equipements").css({"display":"block"});
    $('html, body').animate({
        scrollTop: $("#equipements").offset().top
    }, 1000);

    create_table("equipements", $("#equipements_commune_eqpt").val(), $("#nom_usuel_install_eqpt").val(), $("#nom_equipmt_eqpt").val());

  });
  $("#inc_eqpt").on("click", function() {
    incr("eqpt");
    create_table("equipements", $("#equipements_commune_eqpt").val(), $("#nom_usuel_install_eqpt").val(), $("#nom_equipmt_eqpt").val());
  });
  $("#dec_eqpt").on("click", function() {
    decr("eqpt");
    create_table("equipements", $("#equipements_commune_eqpt").val(), $("#nom_usuel_install_eqpt").val(), $("#nom_equipmt_eqpt").val());
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


  $("#activites_commune").autocomplete({
    source : function(requete, reponse){ // les deux arguments représentent les données nécessaires au plugin
      $.ajax({
        url : ip+"/view/commune", // on appelle le script JSON
        dataType : 'json', // on spécifie bien que le type de données est en JSON
        data : {
          commune : $("#activites_commune").val(),
          table : "Activite_db"},
        success : function(donnee){
          var index = 0;
          reponse( $.map( donnee, function( item ){
            if(index < 8) {
              index++;
              return item;
            }
          }) );
        }
      });
    }
  });
  $("#equipements_commune").autocomplete({
    source : function(requete, reponse){ // les deux arguments représentent les données nécessaires au plugin
      $.ajax({
        url : ip+"/view/commune", // on appelle le script JSON
        dataType : 'json', // on spécifie bien que le type de données est en JSON
        data : {
          commune : $("#equipements_commune").val(),
          table : "Equipement_db"},
        success : function(donnee){
          var index = 0;
          reponse( $.map( donnee, function( item ){
            if(index < 8) {
              index++;
              return item;
            }
          }) );
        }
      });
    }
  });
  $("#installations_commune").autocomplete({
    source : function(requete, reponse){ // les deux arguments représentent les données nécessaires au plugin
      $.ajax({
        url : ip+"/view/commune", // on appelle le script JSON
        dataType : 'json', // on spécifie bien que le type de données est en JSON
        data : {
          commune : $("#installations_commune").val(),
          table : "Installation_db"},
        success : function(donnee){
          var index = 0;
          reponse( $.map( donnee, function( item ){
            if(index < 8) {
              index++;
              return item;
            }
          }) );
        }
      });
    }
  });

  //Check to see if the window is top if not then display button
  	$(window).scroll(function(){
  		if ($(this).scrollTop() > 100) {
  			$('.scrollToTop').fadeIn();
  		} else {
  			$('.scrollToTop').fadeOut();
  		}
  	});

  	//Click event to scroll to top
  	$('.scrollToTop').click(function(){
  		$('html, body').animate({scrollTop : 0},800);
  		return false;
  	});

});
