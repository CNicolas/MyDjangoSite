/* 
* @Author: cnicolas
* @Date:   2015-11-04 11:59:14
* @Last Modified by:   cnicolas
* @Last Modified time: 2015-11-18 11:21:48
*/

'use strict';

$(document).ready(function() {
	$('button#answer').click(function() {
		$(this).addClass('hidden');
		$("button#answerSubmit").text("Répondre");
		$('section#section_answer').removeClass('hidden');
	});
	$('button#answerHide').click(function() {
		$('button#answer').removeClass('hidden');
		$(this).parent().parent().addClass('hidden');
		$("input#id_title").val('');
		CKEDITOR.instances.id_content.setData('');
	});

	$("button.editPost").click(function(event) {
		var post = {};
		post['id'] = $(this).data("postid");

		var lipost = $("li#post" + post.id);
		post['title'] = lipost.find('div.post-title').text();
		post['content'] = lipost.find('div.post-content').html();
		console.log(post);

		$("input#postIdInput").val(post.id);
		$("input#id_title").val(post.title);
		$('label[for="id_title"]').addClass("active");
		CKEDITOR.instances.id_content.setData(post.content);

		$("button#answer").click();
		$("button#answerSubmit").text("Modifier");
	});

	$("a.deletePost").click(function(event) {
		var postId = $(this).data("postid");
		$("input#postId").val(postId);
	});
});