<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
    <title>SNS 품앗이 v0.01</title>
    <link rel="stylesheet" href="main.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no, 
    maximum-scale=1.0, minimum-scale=1.0">


<!-- 사진 크기 설정 스크립트 -->
    <script> 
        function resize () {
                console.log('Resizing...');
                console.log(window.innerWidth);
                
                var win = window.innerWidth;
                var rate = 0.325*(win-940) + 269;
                var count = document.getElementsByClassName("leftBox").length;
                console.log(count);
                if (window.innerWidth<940){
                    for(var i=0; i<count; i++){
                        document.getElementsByClassName("leftBox")[i].style.width=rate+"px";
                        document.getElementsByClassName("leftBox")[i].style.height=rate+"px";}
                    }
        }
        window.addEventListener('resize',function () { resize()}, true);
    </script>

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

    
    <script>resize();</script>
</body>
</html>