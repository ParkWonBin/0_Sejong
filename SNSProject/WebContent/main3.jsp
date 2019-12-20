<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>

<html lang="ko">
<head>
	<!--해드 -->
	<%@ include file= "htmltegs/head.jsp" %>
</head>
<body>
    <!--해더 -->
    <%@ include file= "htmltegs/header.jsp" %>
    
    <!-- 네비 : 하이퍼링크 -->
    <nav  id="nav" class="phone">   
            <table>
                <tr>
                    <td class="menu">  <a href="main1.jsp"> 마이페이지</a> </td>    
                    <td class="menu">  <a href="main2.jsp"> 포인트 벌기</a> </td>    
                    <td class="menu_active">  <a href="main3.jsp"> 의뢰 </a> </td>    
                    <td class="menu">  <a href="main4.jsp"> 의뢰현황 </a> </td>     
                </tr>
            </table>
        </nav >
        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   

            <article id="article">

            <div class='topBox'> 
                    <h3>[의뢰]</h3>
                    <h4>포인트를 사용하여  <br>
                        좋아요와 팔로우 의뢰합니다.
                    </h4>  
            </div>

             
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>
             <span>  <a href="main_quest.jsp"> <img class='leftBox' src="https://placeimg.com/510/510/any" ></a></span>


            </article>

        </section>
 
    <!-- 푸터 -->
    <%@ include file= "htmltegs/footer.jsp" %>

    
    <script>resize("leftBox");</script>
</body>
</html>