/*
* @Author: Aku
* @Date:   2015-11-27 10:09:01
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-11-27 12:07:11
*/

'use strict';

function getRandomIntInclusive(min, max) {
  return Math.floor(Math.random() * (max - min +1)) + min;
}

function damageResolved(damage, critical, targetDefense) {
    var isCritical = Math.random() <= (Number(critical) / 100);
    var dmg = Number(damage);
    var res = getRandomIntInclusive(dmg - 5, dmg + 5);
    if (isCritical) {
        res = Math.ceil(res * 1.5);
    }
    res -= res * (Number(targetDefense) / 100);

    console.log(damage, critical, targetDefense, isCritical, targetDefense / 100, res)

    return res;
}

function updateEnnemyAttackUsed(ennemy, attack) {
    var newHealth = ennemy.attr('data-health') + attack.attr('data-health');

    ennemy.attr('data-health', newHealth);

    ennemy.find('.health').text(newHealth);
}

function updateEnnemyAttackUndergone(ennemy, attack) {
    var newHealth = ennemy.attr('data-health') - damageResolved(attack.attr('data-fulldamage'), attack.attr('data-critical'), 0);

    // console.log(ennemy.attr('data-health'), ennemy.find('.health').text(), newHealth);

    ennemy.attr('data-health', newHealth);

    ennemy.find('.health').text(newHealth);
}

function updatePlayerAttackUsed(player, attack) {
    var newHealth = Number(player.attr('data-health')) + Number(attack.attr('data-heal'));
    var newMana = Number(player.attr('data-mana')) - Number(attack.attr('data-mana'));
    var newEnergy = Number(player.attr('data-energy')) - Number(attack.attr('data-energy'));

    // console.log(player.attr('data-health'), player.find('.health').text(), newHealth);

    player.attr('data-health', newHealth);
    player.attr('data-mana', newMana);
    player.attr('data-energy', newEnergy);

    player.find('.health').text(newHealth);
    player.find('.mana').text(newMana);
    player.find('.energy').text(newEnergy);
}

function updatePlayerAttackUndergone(player, attack) {
    var newHealth = player.attr('data-health') - damageResolved(attack.attr('data-damage'), attack.attr('data-critical'), player.attr('data-defense'));

    // console.log(player.attr('data-health'), player.find('.health').text(), newHealth);

    player.attr('data-health', newHealth);

    player.find('.health').text(newHealth);
}

$(document).ready(function() {
    $("button.attack").each(function(index, el) {
        var jEl = $(el);
        if (jEl.data('name').length > 11) {
            jEl.text(jEl.data('acronym'));
        }
    });

    var playerAttack = {};
    var player = {};
    $("button.attack").click(function(event) {
        var button = $(this);
        player = button.parents("div.player");
        playerAttack = button;

        $("div.ennemy").unbind('click');
        $("div.ennemy").click(function(event) {
            var ennemy = $(this);

            updateEnnemyAttackUndergone(ennemy, playerAttack);

            updatePlayerAttackUsed(player, playerAttack);

            playerAttack = {};
            player = {};
            $(this).unbind('click');

            var ennemyAttacks = ennemy.find('div.attacks .row button');
            var alea = getRandomIntInclusive(1, ennemyAttacks.length);
            updatePlayerAttackUndergone(player, ennemyAttacks[alea])
        });
    });
});
