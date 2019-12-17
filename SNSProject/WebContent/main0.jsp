
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>SNS 품앗이 v0.01</title>
    <link rel="stylesheet" href="main.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, 
    maximum-scale=1.0, minimum-scale=1.0">
    
</head>
<body>
<<<<<<< HEAD
    <!-- 해더 : 새로고침 -->
    <header id="header" class="phone">  
        <a onClick="window.location.reload()" style="cursor: pointer;">SNS 품앗이 v0.01 </a>
        
    </header> 
=======

		<%@ Include file="tegs/HeaderNav.jsp" %>

>>>>>>> b4780085d3e0f36ec026c5e8d39114529aac2999
        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   


            <article id="article">
<<<<<<< HEAD
            
                <div class="loginBox_Photo">
                   <img  src="https://placeimg.com/150/150/any" >
=======
                <div style="background-color: gray; border-radius: 50%; height:250px; width: 250px; margin: 50px 0px; display: inline-block;"></div>
                   
                <div class='loginBox'> <h3>Like Exchanger <br> 좋아요, 팔로우 서비스 </h3> </div>
                <div class='loginBox'> <a href="login/login.jsp"> <h3> 로그인 </h3> </a> </div>
                <div class='loginBox'> <h4> 로그인 시 약관 동의로 간주 <br> 약관 바로가기 </h4> </div>

>>>>>>> b4780085d3e0f36ec026c5e8d39114529aac2999

                </div>
                
                <div class='loginBox'> <a href="main1.jsp"> <h3>Like Exchanger <br> 좋아요, 팔로우 서비스 </h3> </a> </div>
                <div class='loginBox'>  <a href="login/login.jsp"> <h3>로그인</h3> </a> </div>
                <div class='loginBox'> <h4> 로그인 시 약관 동의로 간주 <br> 약관 바로가기 </h4> </div>

            </article>
        </section>
        
    <!-- 푸터 -->
    <%@ include file= "htmltegs/footer.jsp" %>
</body>
</html>