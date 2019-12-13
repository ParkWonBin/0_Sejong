<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="utf-8">
<head>
    <title>SNS 품앗이 v0.01</title>
    <link rel="stylesheet" href="main.css" />
</head>
<body>
    <!-- 해더 : 새로고침 -->
    <header id="header" class="phone">  
        <a onClick="window.location.reload()" style="cursor: pointer;">SNS 품앗이 v0.01 </a>
    </header> 
    <!-- 네비 : 하이퍼링크 -->
    <nav  id="nav" class="phone">   
        <div class="menu">  <a href="main1.jsp"> 마이페이지</a> </div>    
        <div class="menu">  <a href="main2.jsp"> 포인트 벌기</a> </div>    
        <div class="menu">  <a href="main3.jsp"> 의뢰 </a> </div>    
        <div class="menu">  <a href="main4.jsp"> 의뢰현황 </a> </div>     
    </nav >
        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   


            <article id="article">
                <div style="background-color: gray; border-radius: 50%; height:250px; width: 250px; margin: 50px 0px; display: inline-block;"></div>
                   
                <div class='loginBox'> <h3>Like Exchanger <br> 좋아요, 팔로우 서비스 </h3> </div>
                <div class='loginBox'> <a href="login.jsp"> <h3> 로그인 </h3> </a> </div>
                <div class='loginBox'> <h4> 로그인 시 약관 동의로 간주 <br> 약관 바로가기 </h4> </div>



            </article>

        </section>
    <!-- 푸터 : 푸터 -->
    <footer id="footer"class="phone">         
        <h2>C팀 sns 품앗이</h2> 
        <p> Company Name  서울시 노량진 어느 학원 <br>
            사업자등록번호 000-00-00000   전화 000-0000-0000   팩스 00-000-0000</p> 
    </footer>
</body>
</html>