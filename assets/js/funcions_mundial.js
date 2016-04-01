function create2DArray(rows) {
  var arr = [];

  for (var i=0;i<rows;i++) {
     arr[i] = [];
  }

  return arr;
}

function genera_resultats(formulari)
{
    var resultats = create2DArray(25);

    for (var i=0; i<6; i++)
    {
        var id_equip1 = parseInt(formulari.elements["form-"+i+"-equip-1"].value);
        var id_equip2 = parseInt(formulari.elements["form-"+i+"-equip-2"].value);
        var gols_equip1 = parseInt(formulari.elements["form-"+i+"-gols1"].value)
        var gols_equip2 = parseInt(formulari.elements["form-"+i+"-gols2"].value)
        resultats[id_equip1][id_equip2] = gols_equip1;
        resultats[id_equip2][id_equip1] = gols_equip2;
    }
    return resultats;
}

function ordena(ids_equips, resultats)
{
    var equips = []
    for (var i = 0; i<ids_equips.length; i++)
    {
        equips.push({'id': ids_equips[i], 'punts': 0, 'gols': 0, 'diferencia': 0});
    }

    for (var i = 0; i<ids_equips.length; i++)
    {
        for (var j = i + 1; j<ids_equips.length; j++)
        {
            id_equip1 = ids_equips[i];
            id_equip2 = ids_equips[j];

            gols_equip1 = resultats[id_equip1][id_equip2];
            gols_equip2 = resultats[id_equip2][id_equip1];
       
            // Actualitza punts
            if (gols_equip1 > gols_equip2)
            {
               _.findWhere(equips, {'id':id_equip1}).punts += 3;
            }
            else if (gols_equip2 > gols_equip1)
            {
               _.findWhere(equips, {'id':id_equip2}).punts += 3;
            }
            else
            {
               _.findWhere(equips, {'id':id_equip1}).punts += 1;
               _.findWhere(equips, {'id':id_equip2}).punts += 1;
            }
            
            // Actualitza diferencia i gols
            _.findWhere(equips, {'id':id_equip1}).gols += gols_equip1;
            _.findWhere(equips, {'id':id_equip2}).gols += gols_equip2;
            
            _.findWhere(equips, {'id':id_equip1}).diferencia += gols_equip1;
            _.findWhere(equips, {'id':id_equip2}).diferencia += gols_equip2;
            
            _.findWhere(equips, {'id':id_equip1}).diferencia -= gols_equip2;
            _.findWhere(equips, {'id':id_equip2}).diferencia -= gols_equip1;
        }
    }

    return _(equips).chain().sortBy('gols').sortBy('diferencia').sortBy('punts').reverse().value();
}

function classifica(ids_equips, resultats)
{
    var error = 0;
    var classificats = ordena(ids_equips, resultats);

    var agrupats = _.groupBy(classificats, function(obj){ return obj.punts+"-"+obj.diferencia+"-"+obj.gols; });
    if (Object.keys(agrupats).length == ids_equips.length)
    {
        return [classificats, error];
    }
    else if (Object.keys(agrupats).length == 1)
    {
        error = 1;
    }
    else
    {
        var new_classificats = Array();
        for (var i = 0; i < Object.keys(agrupats).length; i++)
	{
	    if (agrupats[Object.keys(agrupats)[i]].length == 1)
	    {
	        new_classificats.push(agrupats[Object.keys(agrupats)[i]][0]);
	    }
	    else
	    {
		var sub_ids = Array();
		for (var j = 0; j < agrupats[Object.keys(agrupats)[i]].length; j++)
		{
		    sub_ids.push(agrupats[Object.keys(agrupats)[i]][j].id);
		}
	        var resultat_sub_classifica = classifica(sub_ids, resultats);
		var sub_classifica = resultat_sub_classifica[0];
		error = resultat_sub_classifica[1];

		for (var j = 0; j < sub_classifica.length; j++)
		{
		    new_classificats.push(_.findWhere(classificats, {'id':sub_classifica[j].id}));
		}
	    }
	}
	classificats = new_classificats;
    }
        
    return [classificats, error];
}

function actualitza()
{
    var formulari = document.getElementById("f1");
    var ids_equips = [
        parseInt(formulari.elements["form-0-equip-1"].value),
        parseInt(formulari.elements["form-0-equip-2"].value),
        parseInt(formulari.elements["form-1-equip-1"].value),
        parseInt(formulari.elements["form-1-equip-2"].value)
    ]

    var noms_equips = Array(25);
    var banderes_equips = Array(25);
    for (var i = 0; i<ids_equips.length; i++)
    {
       noms_equips[ids_equips[i]] = formulari.elements["nom-equip-"+ids_equips[i]].value
       banderes_equips[ids_equips[i]] = formulari.elements["bandera-equip-"+ids_equips[i]].value
    }

    resultats = genera_resultats(formulari);

    var resultat_classificats = classifica(ids_equips, resultats);
    var classificats = resultat_classificats[0];
    var error = resultat_classificats[1];

    document.ban0.src = banderes_equips[classificats[0].id];
    document.ban1.src = banderes_equips[classificats[1].id];
    document.ban2.src = banderes_equips[classificats[2].id];
    document.ban3.src = banderes_equips[classificats[3].id];

    formulari.elements["c0"].value = noms_equips[classificats[0].id];
    formulari.elements["c1"].value = noms_equips[classificats[1].id];
    formulari.elements["c2"].value = noms_equips[classificats[2].id];
    formulari.elements["c3"].value = noms_equips[classificats[3].id];

    formulari.elements["p0"].value = classificats[0].punts;
    formulari.elements["p1"].value = classificats[1].punts;
    formulari.elements["p2"].value = classificats[2].punts;
    formulari.elements["p3"].value = classificats[3].punts;

    formulari.elements["d0"].value = classificats[0].diferencia;
    formulari.elements["d1"].value = classificats[1].diferencia;
    formulari.elements["d2"].value = classificats[2].diferencia;
    formulari.elements["d3"].value = classificats[3].diferencia;

    formulari.elements["g0"].value = classificats[0].gols;
    formulari.elements["g1"].value = classificats[1].gols;
    formulari.elements["g2"].value = classificats[2].gols;
    formulari.elements["g3"].value = classificats[3].gols;

    if (error == 1)
    {
        alert("ERROOOOR!");
    }
}