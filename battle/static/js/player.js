/*
* @Author: Aku
* @Date:   2015-11-20 15:04:11
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-11-26 12:07:16
*/

'use strict';

$(document).ready(function() {
	$("div.armor-piece").hover(function(event) {
		var data = $(this).data()
		var stats = $("ul.armor-statistics");

		stats.find("span.armor-name").text(data.name);
		stats.find("span.armor-price").text(data.price);
		stats.find("span.armor-defense").text(data.defense);
		stats.find("span.armor-health").text(data.health);
		stats.find("span.armor-mana").text(data.mana);
		stats.find("span.armor-energy").text(data.energy);
		stats.find("span.armor-strength").text(data.strength);
		stats.find("span.armor-agility").text(data.agility);
		stats.find("span.armor-intellect").text(data.intellect);
		stats.find("span.armor-spirit").text(data.spirit);
	});
});
