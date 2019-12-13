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
        <div class="menu_active">  <a href="main1.jsp"> 마이페이지</a> </div>    
        <div class="menu">  <a href="main2.jsp"> 포인트 벌기</a> </div>    
        <div class="menu">  <a href="main3.jsp"> 의뢰 </a> </div>    
        <div class="menu">  <a href="main4.jsp"> 의뢰현황 </a> </div>     
    </nav >
        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   

            <article id="article">

                <div class="MyPageBox">
                    <table class="Profile">
                        <tr>
                            <th rowspan="3"><div class="Profile_Photo"></div></th>
                            <td>이름</td>
                            <td>포인트</td>
                            <td>충전</td>
                        </tr>
                        <tr>
                            <td>팔로우</td>
                            <td>좋아요</td>
                            <td>게시글</td>
                        </tr>
                        <tr>
                            <td>30</td>
                            <td>50</td>
                            <td>10</td>
                        </tr>
                    </table>
                </div>
                <div class="MyPageBox"> <h3>공지사항</h3> </div>
                <div class="MyPageBox"> <h3>실시간 문의</h3> </div>
                <div class="MyPageBox"> <h3>친구에게 공유</h3> </div>
                <div class="MyPageBox"> <a href="main0.jsp"> <h3>로그아웃</h3> </a> </div>

            </article>

        </section>
    <!-- 푸터 : 푸터 -->
    <footer id="footer"class="phone">         
        <h2>C팀 sns 품앗이</h2> 
        <p> Company Name  서울시 노량진 어느 학원 <br>
            사업자등록번호 000-00-00000   전화 000-0000-0000   팩스 00-000-0000</p> 
    </footer>

    <script> resize(); </script>
</body>
</html>