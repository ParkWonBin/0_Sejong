<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
    <title>SNS 품앗이 v0.01</title>
    <link rel="stylesheet" href="main.css" />
    
<!-- 사진 크기 설정 스크립트 -->
    <script> 
        function resize () {
                console.log('Resizing...');
                console.log(window.innerWidth);
                
                var win = window.innerWidth;
                var rate = 0.35*(win-940) + 269;
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
    <!-- 해더 : 새로고침 -->
    <header id="header" class="phone">  
        <a onClick="window.location.reload()" style="cursor: pointer;">SNS 품앗이 v0.01 </a>
    </header> 
    <!-- 네비 : 하이퍼링크 -->
    <nav  id="nav" class="phone">   
        <div class="menu">  <a href="main1.jsp"> 마이페이지</a> </div>    
        <div class="menu">  <a href="main2.jsp"> 포인트 벌기</a> </div>    
        <div class="menu_active">  <a href="main3.jsp"> 의뢰 </a> </div>    
        <div class="menu">  <a href="main4.jsp"> 의뢰현황 </a> </div>    
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

                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>
                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>
                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>            
                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>
                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>
                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>      
                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>
                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>
                <div class='leftBox'> 
                        <h2>What is Lorem Ipsum? </h2>
                        <h5>Title description, Dec 7, 2017</h5>  
                </div>      
            </article>

        </section>
    <!-- 푸터 : 푸터 -->
    <footer id="footer"class="phone">         
        <h2>C팀 sns 품앗이</h2> 
        <p> Company Name  서울시 노량진 어느 학원 <br>
            사업자등록번호 000-00-00000   전화 000-0000-0000   팩스 00-000-0000</p> 
    </footer>
    
    <script>resize();</script>
</body>
</html>