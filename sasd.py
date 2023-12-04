web_string = """
<!DOCTYPE html
    PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns=http://www.w3.org/1999/xhtml><!--
 Page saved with SingleFile 
 url: https://inv-veri.chinatax.gov.cn/cyjg10.html 
 saved date: Thu Nov 30 2023 21:33:42 GMT+0800 (中国标准时间)
-->
<meta charset=utf-8>
<meta http-equiv=X-UA-Compatible content="IE=edge">
<meta http-equiv=pragma content=no-cache>
<meta http-equiv=Cache-Control content="no-cache, must-revalidate">
<meta http-equiv=expires content=0>
<meta name=viewport content="width=device-width">
<meta name=keywords content>
<meta name=description content="A jQuery plugin to add qr codes to your pages">
<style>
    body,
    h1,
    td,
    p {
        margin: 0;
        padding: 0
    }

    h1 {
        font-size: 100%
    }

    table,
    tbody,
    tr,
    td {
        text-align: inherit;
        line-height: inherit;
        font-size: 100%
    }

    table {
        border-collapse: collapse;
        border-spacing: 0
    }

    tbody {
        display: table-row-group
    }

    tr {
        display: table-row
    }

    td {
        display: table-cell
    }

    p {
        line-height: 20px;
        clear: both;
        overflow: hidden
    }

    h1 {
        font: normal 18px"MicroSoft YaHei", "SimHei";
        margin-top: 5px;
        clear: both;
        overflow: hidden
    }

    .clearfix:after,
    .main:after {
        content: ".";
        display: block;
        height: 0;
        clear: both;
        visibility: hidden
    }

    .clearfix {
        display: block
    }

    body {
        background-color: #f2f2f2;
        font: normal 14px"MicroSoft YaHei", "SimHei";
        color: #000
    }

    #content {
        margin: 0 auto;
        text-align: left;
        position: relative
    }

    #content .title {
        background: none;
        color: #000;
        font: bold 20px/38px"MicroSoft YaHei", "SimHei"
    }

    #content {
        background: #fff;
        width: 1028px;
        padding: 36px
    }

    .warp {
        word-wrap: break-word;
        word-break: break-all;
        width: 350px
    }

    .comm_table2 {
        margin: 0 auto
    }

    .comm_table2 td {
        padding: 10px;
        text-align: left;
        font-size: 16px
    }

    .fppy_table,
    .fppy_table td {
        border: 1px solid #aaa;
        border-collapse: collapse;
        line-height: 25px;
        background: #fafafa;
        margin: 0 auto
    }

    .fppy_table td.borderNo {
        border: 0px
    }

    .fppy_table td.borderRight {
        border-left: 0px
    }

    table.fppy_table_box {
        border: 0px;
        border-collapse: collapse
    }

    table.fppy_table_box td {
        border: 0px solid #ccc;
        border-collapse: collapse
    }

    .fppy_table_box td.borderTop {
        border-top: 1px solid #aaa
    }

    .fppy_table_box td.borderRight {
        border-right: 1px solid #aaa
    }

    .align_center {
        text-align: center !important
    }

    .align_left {
        text-align: left !important;
        padding: 0 3px 0 3px
    }

    .align_right {
        text-align: right !important;
        padding: 0 3px 0 3px
    }

    .content_td_blue {
        color: #574B9D
    }
</style>
<div id=cms_r>
        <div class=cms_r_main>
            <div class=chayan_div>
                <div id=print_area class=printdiv>
                    <table border=1 class=comm_table2 width=100%>
                        <tbody>
                            <tr>
                                <td colspan=4 style=background-color:#015293;color:#fff;line-height:40px><span
                                        id=cycs>查验次数：第{cycs}次</span>
                                    <span style=padding-left:50px id=cysj>查验时间：{cysj}</span>
                                    <span style=float:right>
                                </td>
                            </tr>
                    </table>
                        <div class=tab-page id=tabPage-dzfp style=display:block>
                            <div>
                                <span class=content_td_blue style=font-size:16px;display:inline id=dkbz></span>
                                <h1 id=fpcc_dzfp
                                    style="color:#015293;padding:5px 0px 5px 0px;text-align:center;position:relative">
                                    {fpcc_dzfp}</h1>
                            </div>
                            <table border=0 cellpadding=0 cellspacing=0 style=width:100%>
                                <tbody>
                                    <tr height=30>
                                        <td class=align_left>发票代码：<span class=content_td_blue
                                                id=fpdm_dzfp>{fpdm}</span></td>
                                        <td>&nbsp;</td>
                                        <td class=align_left>发票号码：<span class=content_td_blue
                                                id=fphm_dzfp>{fphm}</span></td>
                                        <td>&nbsp;</td>
                                        <td class=align_left>开票日期：<span class=content_td_blue
                                                id=kprq_dzfp>{kprq}</span></td>
                                        <td>&nbsp;</td>
                                        <td class=align_left>校验码：<span class=content_td_blue
                                                id=jym_dzfp>{jym}</span></td>
                                        <td>&nbsp;</td>
                                        <td class=align_left>机器编号：<span class=content_td_blue
                                                id=sbbh_dzfp>{sbbh}</span></td>
                                        <td>&nbsp;</td>
                                    </tr>
                            </table>
                            <table style=width:100% border=0 cellspacing=0 cellpadding=0 class=fppy_table>
                                <tbody>
                                    <tr>
                                        <td rowspan=4 class=align_center width=20>
                                            <p>购</p>
                                            <p>买</p>
                                            <p>方</p>
                                        </td>
                                        <td class="align_left borderNo" width=105>名称：</td>
                                        <td nowrap class="align_left borderNo bgcolorWhite"><span class=content_td_blue
                                                id=gfmc_dzfp>{gfmc}</span></td>
                                        <td rowspan=4 class=align_center width=20>
                                            <p>密</p>
                                            <p>码</p>
                                            <p>区</p>
                                        </td>
                                        <td rowspan=4 nowrap class=align_left width=350 id=password_dzfp>&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td class="align_left borderNo">纳税人识别号：</td>
                                        <td nowrap class="align_left borderNo"><span class=content_td_blue
                                                id=gfsbh_dzfp>{gfsbh}</span></td>
                                    </tr>
                                    <tr>
                                        <td class="align_left borderNo" valign=top>地址、电话：</td>
                                        <td class="align_left borderNo" valign=top><span class=content_td_blue
                                                id=gfdzdh_dzfp>{gfdzdh}</span></td>
                                    </tr>
                                    <tr>
                                        <td class="align_left borderNo" valign=top>开户行及账号：</td>
                                        <td class="align_left borderNo" valign=top><span class=content_td_blue
                                                id=gfyhzh_dzfp>{gfyhzh}</span></td>
                                    </tr>
                                    <tr>
                                        <td colspan=5>
                                            <table cellspacing=0 cellpadding=0 style=width:100% class=fppy_table_box>
                                                <tbody>
                                                    <tr id=tab_head_dzfp>
                                                        <td class="align_center borderRight" width=30%>货物或应税劳务、服务名称</td>
                                                        <td class="align_center borderRight" width=10%>规格型号</td>
                                                        <td class="align_center borderRight" width=5%>单位</td>
                                                        <td class="align_center borderRight" width=10%>数量</td>
                                                        <td class="align_center borderRight" width=10%>单价</td>
                                                        <td class="align_center borderRight" width=15%>金额</td>
                                                        <td class="align_center borderRight" width=5%>税率</td>
                                                        <td class=align_center width=15%>税额</td>
                                                    <tr>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue>*电信服务*通信服务费</span>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue>108.30</span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue>0%</span>
                                                        <td class=align_right><span class=content_td_blue>0.00</span>
                                                    </tr>
                                                    <tr>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue>*电信服务*通信服务费</span>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue>108.30</span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue>0%</span>
                                                        <td class=align_right><span class=content_td_blue>0.00</span>
                                                    <tr>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue>*电信服务*通信服务费</span>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_left borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue></span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue>108.30</span>
                                                        <td class="align_right borderRight"><span
                                                                class=content_td_blue>0%</span>
                                                        <td class=align_right><span class=content_td_blue>0.00</span>
                                                    <tr>
                                                        <td class="align_center borderRight">合计</td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class="align_right borderRight"><span class=content_td_blue
                                                                id=je_dzfp>￥{je}</span></td>
                                                        <td class="align_center borderRight">&nbsp;</td>
                                                        <td class=align_right><span class=content_td_blue
                                                                id=se_dzfp>￥{se}</span></td>
                                                    </tr>
                                                    <tr>
                                                        <td class="align_center borderRight borderTop">价税合计（大写）</td>
                                                        <td colspan=4 class="align_left borderTop"><span
                                                                class=align_left><span class=content_td_blue
                                                                    id=jshjdx_dzfp>⊗{jshjdx}</span></span></td>
                                                        <td colspan=3 class="align_left borderTop"><span
                                                                style="padding:0 20px">（小写）</span><span
                                                                class=content_td_blue id=jshjxx_dzfp>￥{jshjxx}</span></td>
                                                    </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td rowspan=4 class=align_center>
                                            <p>销</p>
                                            <p>售</p>
                                            <p>方</p>
                                        </td>
                                        <td class="align_left borderNo">名称：</td>
                                        <td class="align_left borderNo"><span class=content_td_blue
                                                id=xfmc_dzfp>中国联合网络通信有限公司北京市分公司</span></td>
                                        <td rowspan=4 class=align_center width=20>
                                            <p>备</p>
                                            <p>注</p>
                                        </td>
                                        <td rowspan=4 class="align_left content_td_blue" width=350 id=bz_dzfp
                                            valign=top>
                                            <p class=warp>{bz}</p>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="align_left borderNo">纳税人识别号：</td>
                                        <td class="align_left borderNo"><span class=content_td_blue
                                                id=xfsbh_dzfp>{xfsbh}</span></td>
                                    </tr>
                                    <tr>
                                        <td class="align_left borderNo">地址、电话：</td>
                                        <td class="align_left borderNo"><span class=content_td_blue
                                                id=xfdzdh_dzfp>{xfdzdh}</span></td>
                                    </tr>
                                    <tr>
                                        <td class="align_left borderNo">开户行及账号：</td>
                                        <td class="align_left borderNo"><span class=content_td_blue
                                                id=xfyhzh_dzfp>{xfyhzh}</span></td>
                                    </tr>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
""".format(cycs="1", cysj="2023-12-05 ")