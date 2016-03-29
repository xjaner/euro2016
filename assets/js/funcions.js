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

    for (i=0; i<6; i++)
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

function classifica(ids_equips, resultats)
{
    var equips = []
    for (i = 0; i<ids_equips.length; i++)
    {
        equips.push({'id': ids_equips[i], 'punts': 0, 'gols': 0, 'diferencia': 0});
    }

    for (i = 0; i<ids_equips.length; i++)
    {
        for (j = 1; j<ids_equips.length; j++)
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

    return _(equips).chain().sortBy('gols').sortBy('diferencia').sortBy('punts').reverse();
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
    for (i = 0; i<ids_equips.length; i++)
    {
    	noms_equips[ids_equips[i]] = formulari.elements["nom-equip-"+ids_equips[i]]
    }

    resultats = genera_resultats(formulari);

    classificats = classifica(ids_equips, resultats);

    formulari.elements["c0"].value = classificats[0].id
    formulari.elements["c1"].value = classificats[1].id
    formulari.elements["c2"].value = classificats[2].id
    formulari.elements["c3"].value = classificats[3].id
}
