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

        <div class="white_space"></div>

            <article id="article">
            
                 <div class="loginBox_Photo"><img src="https://placeimg.com/200/200/any" ></div>
                
                <div class='loginBox'> <a href="main1.jsp"> <h3>Like Exchanger <br> 좋아요, 팔로우 서비스 </h3> </a> </div>
               

            <!-- 회원가입 화면 -->
            <div class="jumbotron" style="padding-top: 20px;">
				<form method="post" action="loginAction.jsp">
					<h3 style="text-align: center;">회원가입 화면</h3>
					<div class="form-group">
						<input type="text" class="form-control" placeholder="아이디" name="userID" maxlength="20">
					</div>
					<div class="form-group">
						<input type="password" class="form-control" placeholder="비밀번호" name="userPassword" maxlength="20">
					</div>
					<div class="form-group">
						<input type="text" class="form-control" placeholder="인스타아이디" name="instaID" maxlength="20">
					</div>
					<div class="form-group">
						<input type="password" class="form-control" placeholder="인스타비밀번호" name="instaPassword" maxlength="20">
					</div>
					<input type="submit" class="btn btn-primary form-control" value="회원가입" >
				</form>
			</div>    
                <div class='loginBox'> <h4> 로그인 시 약관 동의로 간주 <br> 약관 바로가기 </h4> </div>

            </article>

<div class="white_space"></div>
        </section>
    <!-- 푸터 -->
    <%@ include file= "htmltegs/footer.jsp" %>
    
    
   	<script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
	<script src="js/bootstrap.js"></script>
    
</body>
</html>