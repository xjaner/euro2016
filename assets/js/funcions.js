function create2DArray(rows) {
  var arr = [];

  for (var i=0;i<rows;i++) {
     arr[i] = [];
  }

  return arr;
}

function actualitza()
{
    var resultats = create2DArray(25);
    var formulari = document.getElementById("f1");
    var ids_equips = [
        parseInt(formulari.elements["form-0-equip-1"].value),
        parseInt(formulari.elements["form-0-equip-2"].value),
        parseInt(formulari.elements["form-1-equip-1"].value),
        parseInt(formulari.elements["form-1-equip-2"].value)
    ]

    var equips = []
    for (i = 0; i<ids_equips.length; i++)
    {
        equips.push({'id': ids_equips[i], 'punts': 0, 'gols': 0, 'diferencia': 0});
    }

    for (i=0; i<6; i++)
    {
        var id_equip1 = parseInt(formulari.elements["form-"+i+"-equip-1"].value);
        var id_equip2 = parseInt(formulari.elements["form-"+i+"-equip-2"].value);
        var gols_equip1 = parseInt(formulari.elements["form-"+i+"-gols1"].value)
        var gols_equip2 = parseInt(formulari.elements["form-"+i+"-gols2"].value)
        resultats[id_equip1][id_equip2] = gols_equip1;
        resultats[id_equip2][id_equip1] = gols_equip2;

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
