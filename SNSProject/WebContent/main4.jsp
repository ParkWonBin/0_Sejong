<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="utf-8">
<head>
    <title>SNS 품앗이 v0.01</title>
    <link rel="stylesheet" href="main.css" />


    <script> 
        function resize () {
            console.log('Resizing...');
            console.log(window.innerWidth);
            
            var win = window.innerWidth;
            var rate = 0.35*(win-940) + 269;
            var count = document.getElementsByClassName("Qtable_Photo").length;
            console.log(count);
            if (window.innerWidth<940){
                for(var i=0; i<count; i++){
                    document.getElementsByClassName("Qtable_Photo")[i].style.width=rate+"px";
                    document.getElementsByClassName("Qtable_Photo")[i].style.height=rate+"px";}
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
        <div class="menu">  <a href="main3.jsp"> 의뢰 </a> </div>    
        <div class="menu_active">  <a href="main4.jsp"> 의뢰현황 </a> </div>     
    </nav >
        <!-- Section : 내부에 article 있음-->
        <section id="section" class="phone" >   

            <!-- 게시글 -->
            
            <article id="article" >

                    <div class='topBox'> 
                            <h4>현재 진행 중인 의뢰 현황을  수 있습니다.</h4>  
                    </div>

                    <table class="Qtable">
                        <th colspan="2" class="Qtable_Photo" ></th>
                        <tr>
                            <th class="Qtable_left" >[진행]</th>
                            <th class="Qtable_right">10%</th>
                        </tr>
                        <tr>
                            <td colspan="2" class="Qtable_bar" >
                                <div class="Qtable_bar_inside"></div>
                            </td>
                        </tr>
                        <tr>
                            <th class="Qtable_left">[좋아요]</th>
                            <th class="Qtable_right">10/100</th>
                        </tr>
                    </table>

                    
                    <table class="Qtable">
                        <th colspan="2" class="Qtable_Photo" ></th>
                        <tr>
                            <th class="Qtable_left" >[진행]</th>
                            <th class="Qtable_right">10%</th>
                        </tr>
                        <tr>
                            <td colspan="2" class="Qtable_bar" >
                                <div class="Qtable_bar_inside"></div>
                            </td>
                        </tr>
                        <tr>
                            <th class="Qtable_left">[좋아요]</th>
                            <th class="Qtable_right">10/100</th>
                        </tr>
                    </table>

                    
                    <table class="Qtable">
                        <th colspan="2" class="Qtable_Photo" ></th>
                        <tr>
                            <th class="Qtable_left" >[진행]</th>
                            <th class="Qtable_right">10%</th>
                        </tr>
                        <tr>
                            <td colspan="2" class="Qtable_bar" >
                                <div class="Qtable_bar_inside"></div>
                            </td>
                        </tr>
                        <tr>
                            <th class="Qtable_left">[좋아요]</th>
                            <th class="Qtable_right">10/100</th>
                        </tr>
                    </table>

                    
                    <table class="Qtable">
                        <th colspan="2" class="Qtable_Photo" ></th>
                        <tr>
                            <th class="Qtable_left" >[진행]</th>
                            <th class="Qtable_right">10%</th>
                        </tr>
                        <tr>
                            <td colspan="2" class="Qtable_bar" >
                                <div class="Qtable_bar_inside"></div>
                            </td>
                        </tr>
                        <tr>
                            <th class="Qtable_left">[좋아요]</th>
                            <th class="Qtable_right">10/100</th>
                        </tr>
                    </table>

                    
                    <table class="Qtable">
                        <th colspan="2" class="Qtable_Photo" ></th>
                        <tr>
                            <th class="Qtable_left" >[진행]</th>
                            <th class="Qtable_right">10%</th>
                        </tr>
                        <tr>
                            <td colspan="2" class="Qtable_bar" >
                                <div class="Qtable_bar_inside"></div>
                            </td>
                        </tr>
                        <tr>
                            <th class="Qtable_left">[좋아요]</th>
                            <th class="Qtable_right">10/100</th>
                        </tr>
                    </table>

                    
                    <table class="Qtable">
                        <th colspan="2" class="Qtable_Photo" ></th>
                        <tr>
                            <th class="Qtable_left" >[진행]</th>
                            <th class="Qtable_right">10%</th>
                        </tr>
                        <tr>
                            <td colspan="2" class="Qtable_bar" >
                                <div class="Qtable_bar_inside"></div>
                            </td>
                        </tr>
                        <tr>
                            <th class="Qtable_left">[좋아요]</th>
                            <th class="Qtable_right">10/100</th>
                        </tr>
                    </table>


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