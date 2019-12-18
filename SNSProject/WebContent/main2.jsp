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
                    <td class="menu_active">  <a href="main2.jsp"> 포인트 벌기</a> </td>    
                    <td class="menu">  <a href="main3.jsp"> 의뢰 </a> </td>    
                    <td class="menu">  <a href="main4.jsp"> 의뢰현황 </a> </td>     
                </tr>
            </table>
        </nav >
        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   
            <!-- 게시글 -->
            <div class='topBox'> 
                <h3>[포인트 벌기]</h3>
                <h4>다른 사람 피드입니다.<br>
                    이미지를 선택하여 포인트를 획득하세요.
                </h4>  
            </div>

            <article id="article">

                <span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>
                <span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>
                <span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>
				<span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>
                <span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>
                <span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>
				<span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>
                <span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>
                <span> <img class='leftBox' src="https://placeimg.com/1080/1080/any" ></span>

            </article>

        </section>
        
    <!-- 푸터 -->
    <%@ include file= "htmltegs/footer.jsp" %>

    <script>resize("leftBox");</script>
</body>
</html>