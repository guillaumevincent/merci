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
                    {% raw %}
                    <a class="nav-link bg-primary" v-link="{ path: '/app/' }">
                        {{ $t('index.SIGNIN') }}
                    </a>
                    <a class="nav-link" v-link="{ path: '/register/' }">
                        {{ $t('index.REGISTER') }}
                    </a>
                    {% endraw %}
                </nav>
            </div>
        </div>
        <div id="navbar">
            <div class="container">
                <nav class="navbar">
                    <ul class="nav navbar-nav">
                        <li class="nav-item">
                            {{cookiecutter.project_name}}
                        </li>
                    </ul>
                </nav>
            </div>
        </div>
        <div class="main">
            <div class="container">
                <h1 class="display-3 m-t-3">Amazing Product</h1>

                <p class="lead m-b-3">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ad dolores ea laudantium
                    mollitia nam nostrum odit.</p>

                <div class="row m-b-3">
                    <div class="col-sm-4 m-b-3">
                        <h4>Lorem </h4>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquid aperiam autem,
                            dignissimos eaque, eveniet ex excepturi inventore maiores modi necessitatibus neque nesciunt
                            odit, placeat provident quam repellendus temporibus voluptas?</p>
                    </div>
                    <div class="col-sm-4 m-b-3">
                        <h4>Lorem Ipsum</h4>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut dicta dolores ea eligendi ex
                            fugiat incidunt magni modi, nihil nobis officia possimus quam quas quidem quisquam rerum
                            totam unde voluptate!</p>
                    </div>
                    <div class="col-sm-4 m-b-3">
                        <h4>Ipsum</h4>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deleniti exercitationem in iste,
                            iusto quaerat quam velit vitae? Aliquam aperiam architecto aspernatur delectus, doloremque
                            minus, natus nulla quibusdam ratione repellat unde.</p>
                    </div>
                </div>
                <div class="row m-b-3">
                    <div class="col-sm-4 m-b-3">
                        <h4>Lorem Ipsum</h4>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut dicta dolores ea eligendi ex
                            fugiat incidunt magni modi, nihil nobis officia possimus quam quas quidem quisquam rerum
                            totam unde voluptate!</p>
                    </div>
                    <div class="col-sm-4 m-b-3">
                        <h4>Lorem </h4>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium aliquid aperiam autem,
                            dignissimos eaque, eveniet ex excepturi inventore maiores modi necessitatibus neque nesciunt
                            odit, placeat provident quam repellendus temporibus voluptas?</p>
                    </div>
                    <div class="col-sm-4 m-b-3">
                        <h4>Ipsum</h4>
                        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Deleniti exercitationem in iste,
                            iusto quaerat quam velit vitae? Aliquam aperiam architecto aspernatur delectus, doloremque
                            minus, natus nulla quibusdam ratione repellat unde.</p>
                    </div>
                </div>
                <div class="text-xs-center m-b-3">
                    <button class="btn btn-primary">let's go !</button>
                </div>
            </div>
        </div>
        <div id="footer">
            <div class="container p-t-1">
                <div class="row">
                    <div class="col-lg-12 text-xs-center">
                        <p>
                            &copy; {{cookiecutter.year}} {{cookiecutter.project_name}}
                            {% raw %}- {{ $t('footer.createdBy') }}{% endraw %}
                            {{cookiecutter.full_name}}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>
