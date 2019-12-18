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
    
        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   


            <article id="article">
            
                 <div class="loginBox_Photo"><img src="https://placeimg.com/200/200/any" ></div>
                
                <div class='loginBox'> <a href="main1.jsp"> <h3>Like Exchanger <br> 좋아요, 팔로우 서비스 </h3> </a> </div>
                <div class='loginBox'>  <a href="login.jsp"> <h3>로그인</h3> </a> </div>
                <div class='loginBox'> <h4> 로그인 시 약관 동의로 간주 <br> 약관 바로가기 </h4> </div>

            </article>
        </section>
        
    <!-- 푸터 -->
    <%@ include file= "htmltegs/footer.jsp" %>
</body>
</html>