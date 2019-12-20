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
		<article>
		
		
		<div class='topBox'> 
			 <h3>[의뢰하기]</h3>
			 <h4> 현재 글에 좋아요를 요청합니다.
			 </h4>  
		</div>

	        
	        
           <div class="jumbotron" style="padding-top: 20px;">
				<form method="post" action="loginAction.jsp">
				
<div class="white_space"></div>
		<img style="width:80%" src="https://placeimg.com/1080/1080/any" >
<div class="white_space"></div>
					<div class="form-group">
						<input type="text" class="form-control" placeholder="목표 수량" name="instaID" maxlength="20">
					</div>
					<div class="form-group">
						<div class="form-control"> <h3 style="display:inline-block ;margin: 6px 0 auto; ">가격 : 100pt</h3> </div>
					</div>
					
					
					<input type="submit" class="btn btn-primary form-control" value="좋아요 신청" >
					<input type="submit" class="btn btn-primary form-control" value="팔로우 신청" >
					
				</form>
			</div>
			
			

				                    
<div class="white_space"></div>
<div class="white_space"></div>
<div class="white_space"></div>
         </article>
      </section>
        
    <!-- 푸터 -->
    <%@ include file= "htmltegs/footer.jsp" %>

    <script>resize("leftBox");</script>
</body>
</html>