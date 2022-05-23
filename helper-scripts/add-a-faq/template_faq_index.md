---
layout: custom
title: titles.faq
permalink: /get-started/faq/index.html
---
{% t global.lang_tag %}
<div class="container description">
    <p>{% t faq.intro %}</p>
</div>
<section class="container">
    <div class="row faq">
        <!-- left two-thirds block-->
        <div class="left two-thirds col-lg-8 col-md-8 col-sm-12 col-xs-12">
            <div class="info-block">
                <div class="row center-xs">
                    <div class="col">
                        <h2>{% t faq.toc %}</h2>
                    </div>
                </div>
                <ul>
                    <li class="category">{% t faq.general %}</li>
                    <ul class="logo">
                        !_! toc_general !_!
                    </ul>
                    <li class="category">{% t faq.advanced %}</li>
                    <ul class="logo">
                        !_! toc_advanced !_!
                    </ul>
                    <li class="category">{% t faq.nodeandwallet %}</li>
                    <ul class="logo">
                        !_! toc_nodeandwallet !_!
                    </ul>
                </ul>
            </div>
        </div>
        <!-- END left two-thirds block-->
        <!-- Right one-third block -->
        <div class="right one-third col-lg-4 col-md-4 col-sm-12 col-xs-12">
            <div class="info-block">
                <div class="row center-xs">
                    <div class="col">
                        <h2>{% t faq.resandhelp %}</h2>
                    </div>
                </div>
                <h3><a href="{{ site.baseurl }}/resources/user-guides/">{% t titles.userguides %}</a></h3>
                    <p>{% t faq.userguides %}</p>
                <h3><a href="{{ site.baseurl }}/resources/developer-guides/">{% t titles.developerguides %}</a></h3>
                    <p>{% t faq.devguides %}</p>
                <h3><a href="https://monero.stackexchange.com/">StackExchange</a></h3>
                    <p>{% t faq.stackexchange %}</p>
                <h3><a href="https://www.reddit.com/r/monerosupport/">r/monerosupport</a></h3>
                    <p>{% t faq.monerosupport %}</p>
                <h3><a href="https://www.monero.how/">Monero.how</a></h3>
                    <p>{% t faq.monerohow %}</p>
            </div>
        </div>
    </div>
        <!-- END Right one-third block -->
</section>
<section class="container">
    <div class="row faq">      
        <!-- full block-->
        <div class="full col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <div class="info-block">
                <div class="row center-xs">
                    <!-- 'General' section-->
                    <div class="col"><h2>{% t faq.general %}</h2></div>
                </div>
                    !_! general !_!
                <div class="row center-xs">
                    <!-- 'Advanced' section-->
                    <div class="col"><h2>{% t faq.advanced %}</h2></div>
                </div>
                    !_! advanced !_!
                <div class="row center-xs">
                    <!-- 'Node and Wallet' section-->
                    <div class="col"><h2>{% t faq.nodeandwallet %}</h2></div>
                </div>
                    !_! nodeandwallet !_!
            </div>
        </div>
        <!-- END full block-->
        <a aria-label="{% t accessibility.arrowup %}" href="#" class="arrow-up"><i></i></a>
    </div>
</section>