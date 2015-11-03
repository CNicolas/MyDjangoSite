/* 
* @Author: cnicolas
* @Date:   2015-10-20 14:43:50
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-10-29 16:11:10
*/

'use strict';

$(document).ready(function(){
	// Init the mobile navbar
	$(".button-collapse").sideNav();
	// Init the parallax
	$('.parallax').parallax();
	// Init the modals
	$(".modal-trigger").leanModal();
	$("#modal-connection").closeModal();
	// Init date pickers
	$('.datepicker').pickadate({
		monthsFull: ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
		monthsShort: ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'],
		weekdaysFull: ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'],
		weekdaysShort: ['dim.', 'lun.', 'mar.', 'mer.', 'jeu.', 'ven.', 'sam.'],
		selectMonths: true,
		selectYears: 129,
		min: new Date(1885, 0, 0),
		max: new Date,
		format: "dd/mm/yyyy"
	});

	// Show toasts
	$("span.error-toast").each(function(ind, val) {
		Materialize.toast(this.innerHTML, 4000, "red");
	});
	$("span.success-toast").each(function(ind, val) {
		Materialize.toast(this.innerHTML, 4000, "light-green");
	});
});