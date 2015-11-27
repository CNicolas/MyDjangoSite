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
    return res;
}

function ennemyAttackUsed(ennemy, attack) {
    var newHealth = Number(ennemy.attr('data-health')) + Number(attack.attr('data-heal'));

    var healthPercent = (newHealth * 100) / Number(ennemy.data('fullhealth'));

    ennemy.attr('data-health', newHealth);

    ennemy.find('.health').text(newHealth);

    ennemy.find('.health').next().find('.determinate').css("width", healthPercent + '%' );
}

function ennemyAttackUndergone(ennemy, attack) {
    var newHealth = ennemy.attr('data-health') - damageResolved(attack.attr('data-fulldamage'), attack.attr('data-critical'), 0);

    ennemy.attr('data-health', newHealth);

    ennemy.find('.health').text(newHealth);
}

function playerAttackUsed(player, attack) {
    var newHealth = Number(player.attr('data-health')) + Number(attack.attr('data-heal'));
    var newMana = Number(player.attr('data-mana')) - Number(attack.attr('data-mana'));
    var newEnergy = Number(player.attr('data-energy')) - Number(attack.attr('data-energy'));

    var healthPercent = (newHealth * 100) / Number(player.data('fullhealth'));
    var manaPercent = (newMana * 100) / Number(player.data('fullmana'));
    var energyPercent = (newEnergy * 100) / Number(player.data('fullenergy'));

    player.attr('data-health', newHealth);
    player.attr('data-mana', newMana);
    player.attr('data-energy', newEnergy);

    player.find('.health').text(newHealth);
    player.find('.mana').text(newMana);
    player.find('.energy').text(newEnergy);

    player.find('.health').next().find('.determinate').css("width", healthPercent + '%' );
    player.find('.mana').next().find('.determinate').css("width", manaPercent + '%' );
    player.find('.energy').next().find('.determinate').css("width", energyPercent + '%' );

    var playerAttacks = player.find('div.attacks .row button');
}

function playerAttackUndergone(player, attack) {
    var newHealth = player.attr('data-health') - damageResolved(attack.attr('data-damage'), attack.attr('data-critical'), player.attr('data-defense'));

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

        $("div.ennemy button").click(function(event) {
            var ennemy = $(this).parent();

            ennemyAttackUndergone(ennemy, playerAttack);

            playerAttackUsed(player, playerAttack);

            var ennemyAttacks = ennemy.find('div.attacks .row button');
            var alea = getRandomIntInclusive(0, ennemyAttacks.length - 1);
            playerAttackUndergone(player, ennemyAttacks.eq(alea))

            ennemyAttackUsed(ennemy, ennemyAttacks.eq(alea));

            playerAttack = {};
            player = {};
            $(this).unbind('click');
        });
    });
});
