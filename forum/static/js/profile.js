/* 
* @Author: cnicolas
* @Date:   2015-11-13 15:35:27
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-11-13 15:54:41
*/

'use strict';

$(document).ready(function() {
	$('.datepicker').pickadate({
		monthsFull: ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'],
		monthsShort: ['janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.', 'août', 'sept.', 'oct.', 'nov.', 'déc.'],
		weekdaysFull: ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'],
		weekdaysShort: ['dim.', 'lun.', 'mar.', 'mer.', 'jeu.', 'ven.', 'sam.'],
		selectMonths: true,
		selectYears: 129,
		min: new Date(1885, 0, 0),
		max: new Date,
		format: "dd/mm/yyyy",
		onClose: function() {
		    $(document.activeElement).blur();
		}
	});
});