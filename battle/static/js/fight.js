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

function damageResolution(damage, critical, targetDefense) {
    var isCritical = Math.random() <= (Number(critical) / 100);
    var dmg = Number(damage);
    var alea = getRandomIntInclusive(dmg - 5, dmg + 5);
    var res = alea;
    if (isCritical) {
        res = Math.ceil(res * 1.5);
    }
    var defenseReduction = Math.floor(res * (Number(targetDefense) / 100));
    res -= defenseReduction;

    console.log(dmg + ' -> ' + alea + ' ' + isCritical + ' ' + defenseReduction + ' = ' + res);
    return res;
}

function healResolution(heal, critical) {
    var isCritical = Math.random() <= (Number(critical) / 100);
    var hl = Number(heal);
    var alea = getRandomIntInclusive(hl - 5, hl + 5);
    var res = alea
    if (isCritical) {
        res = Math.ceil(res * 1.5);
    }
    console.log(hl + ' -> ' + alea + ' ' + isCritical + ' = ' + res);
    return res;
}

function ennemyAttackUsed(ennemy, attack) {
    var newHealth = Number(ennemy.attr('data-health')) + Number(attack.attr('data-heal'));

    var healthPercent = (newHealth * 100) / Number(ennemy.data('fullhealth'));

    ennemy.attr('data-health', newHealth);

    ennemy.find('.health').text(newHealth);

    ennemy.find('.health').next().find('.determinate').css("width", healthPercent + '%' );

    console.log(ennemy.data(), attack.data());
}

function ennemyAttackUndergone(ennemy, attack) {
    if (attack.data('fulldamage') != 0) {
        
    } else {

    }


    var newHealth = Number(ennemy.attr('data-health')) - damageResolution(attack.attr('data-fulldamage'), attack.attr('data-critical'), 0);
    newHealth = newHealth + Number(attack.attr('data-heal'));

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
    playerAttacks.each(function(index, el) {
        var jEl = $(el);
        if (Number(jEl.attr('data-energy')) > newEnergy) {
            jEl.addClass('disabled');
        }
        if (Number(jEl.attr('data-mana')) > newMana) {
            jEl.addClass('disabled');
        }
    });

    console.log(player.data(), attack.data());
}

function playerAttackUndergone(player, attack) {
    if (attack.data('fulldamage') != 0) {
        var newHealth = Number(player.attr('data-health')) - damageResolution(attack.attr('data-damage'), attack.attr('data-critical'), player.attr('data-defense'));
    } else {
        var newHealth = Number(player.attr('data-health')) + healResolution(attack.attr('data-fullheal'), attack.attr('data-critical'));
    }

    var healthPercent = (newHealth * 100) / Number(player.data('fullhealth'));

    player.attr('data-health', newHealth);

    player.find('.health').text(newHealth);

    player.find('.health').next().find('.determinate').css("width", healthPercent + '%' );
}

function ennemiesTurn() {
    $('.ennemy').each(function(index, el) {
        var ennemy = $(el);
        var ennemyAttacks = ennemy.find('div.attacks .row button');
        var alea = getRandomIntInclusive(0, ennemyAttacks.length - 1);
        var attack = ennemyAttacks.eq(alea);

        var players = $(".player");
        if (players.length === 1) {
            playerAttackUndergone(players.eq(0), attack)
        } else if (players.length === 2) {
            if (attack.data('target') === 1) {
                alea = getRandomIntInclusive(0, 1);
                playerAttackUndergone(players.eq(alea), attack)
            } else {
                playerAttackUndergone(players.eq(0), attack)
                playerAttackUndergone(players.eq(1), attack)
            }
        } else {
            if (attack.data('target') === 1) {
                alea = getRandomIntInclusive(0, players.length - 1);
                playerAttackUndergone(players.eq(alea), attack)
            } else if (attack.data('target') == 2) {
                alea = getRandomIntInclusive(0, 1);
                if (alea === 0) {
                    playerAttackUndergone(players.eq(0), attack)
                } else {
                    playerAttackUndergone(players.eq(2), attack)
                }
                playerAttackUndergone(players.eq(1), attack)
            }
        }
        ennemyAttackUsed(ennemy, attack);
    });
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
    $("div.player button.attack").click(function(event) {
        var button = $(this);
        player = button.parents("div.player");
        playerAttack = button;

        $("div.ennemy>button").click(function(event) {
            var ennemy = $(this).parent();

            ennemyAttackUndergone(ennemy, playerAttack);

            playerAttackUsed(player, playerAttack);

            ennemiesTurn();

            playerAttack = {};
            player = {};
            $(this).unbind('click');
        });

        $("div.player>button").click(function(event) {
            var target = $(this).parent();

            playerAttackUndergone(target, playerAttack);

            playerAttackUsed(player, playerAttack);

            ennemiesTurn();

            playerAttack = {};
            player = {};
            $(this).unbind('click');
        });
    });
});
