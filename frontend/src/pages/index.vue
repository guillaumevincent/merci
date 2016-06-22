<style>
    #login-bar {
        background-color: #424242;
        height: 38px;
        color: #F5F5F5;
    }

    #login-bar .nav-link {
        padding-left: 1em;
        padding-right: 1em;
        color: inherit;
    }

    #login-bar .nav-link {
        line-height: 38px;
    }

    #navbar {
        background-color: white;
        border-bottom: 1px solid #e8e8e8;
        margin: 0;
    }

    #navbar #navbar__logo {
        height: 36px;
    }

    #navbar .navbar {
        padding: 1em 0;
    }

    #footer {
        background-color: #424242;
        color: #F5F5F5;
        font-size: 0.8em;
    }

    #footer a {
        color: inherit;
    }
</style>
<template>
    <div id="landing-page">
        <div id="login-bar">
            <div class="container">
                <nav class="nav nav-inline pull-xs-right">
                    <a class="nav-link bg-primary" v-link="{ path: '/app/' }">
                        {{ $t('index.LOGIN') }}
                    </a>
                    <a class="nav-link" v-link="{ path: '/register/' }">
                        {{ $t('index.REGISTER') }}
                    </a>
                </nav>
            </div>
        </div>
        <div id="navbar">
            <div class="container">
                <nav class="navbar">
                    <ul class="nav navbar-nav">
                        <li class="nav-item">
                            Merci
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div id="footer">
            <div class="container p-t-1">
                <div class="row">
                    <div class="col-lg-12 text-xs-center">
                        <p>
                            &copy; Merci
                            - {{ $t('footer.createdBy') }}
                            <a href="https://twitter.com/guillaume20100">Guillaume Vincent</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
