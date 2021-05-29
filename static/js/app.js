$(document).on('click', '#id_submit', function (event) {
	event.preventDefault();
	var ques1= $("input[name='Ques1']:checked").val()
	var ques2= $("input[name='Ques2']:checked").val()
	var ques3= $("input[name='Ques3']:checked").val()
	var ques4= $("input[name='Ques4']:checked").val()
	var ques5= $("input[name='Ques5']:checked").val()
	var ques6= $("input[name='Ques6']:checked").val()
	var ques7= $("input[name='Ques7']:checked").val()
	var ques8= $("input[name='Ques8']:checked").val()
	var comment= document.getElementById('Comment').value;
	alert(comment);
	$.ajax({
		url:"/inputData/",
		type: "Post",
		data : {'ques1' : ques1,'ques2' : ques2,'ques3' : ques3,'ques4' : ques4,'ques5' : ques5,'ques6' : ques6,'ques7' : ques7,'ques8' : ques8,'comment' : comment},
	    success: function(result)
		{
			$("#review").html(result.review);
		},
		error: function(e)
		{
			alert("Error");
		}
		
	});
});