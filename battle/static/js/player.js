/*
* @Author: Aku
* @Date:   2015-11-20 15:04:11
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-11-25 10:14:24
*/

'use strict';

$(document).ready(function() {
	$("div.armor-piece").click(function(event) {
		var datas = $(this).data()
		var stats = $("ul.armor-statistics");

		stats.find("span.armor-name").text(datas.name);
		stats.find("span.armor-price").text(datas.price);
		stats.find("span.armor-defense").text(datas.defense);
		stats.find("span.armor-health").text(datas.health);
		stats.find("span.armor-mana").text(datas.mana);
		stats.find("span.armor-energy").text(datas.energy);
		stats.find("span.armor-strength").text(datas.strength);
		stats.find("span.armor-agility").text(datas.agility);
		stats.find("span.armor-intellect").text(datas.intellect);
		stats.find("span.armor-spirit").text(datas.spirit);
	});
});
