%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-j
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1238:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/garuda-c90.tar.xz
Source1394:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/geometry.tar.xz
Source1395:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/geometry.doc.tar.xz
Source1397:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphics.tar.xz
Source1398:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphics.doc.tar.xz
Source1457:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/geschichtsfrkl.tar.xz
Source1458:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/geschichtsfrkl.doc.tar.xz
Source1864:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/genealogy.tar.xz
Source1865:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/genealogy.doc.tar.xz
Source1866:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gentium-tug.tar.xz
Source1867:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gentium-tug.doc.tar.xz
Source1869:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsartemisia.tar.xz
Source1870:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsartemisia.doc.tar.xz
Source1871:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsbodoni.tar.xz
Source1872:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsbodoni.doc.tar.xz
Source1873:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfscomplutum.tar.xz
Source1874:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfscomplutum.doc.tar.xz
Source1875:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsdidot.tar.xz
Source1876:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsdidot.doc.tar.xz
Source1877:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsneohellenic.tar.xz
Source1878:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsneohellenic.doc.tar.xz
Source1879:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfssolomos.tar.xz
Source1880:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfssolomos.doc.tar.xz
Source1881:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gillcm.tar.xz
Source1882:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gillcm.doc.tar.xz
Source1883:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gillius.tar.xz
Source1884:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gillius.doc.tar.xz
Source1885:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gnu-freefont.tar.xz
Source1886:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gnu-freefont.doc.tar.xz
Source1888:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gothic.tar.xz
Source1889:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gothic.doc.tar.xz
Source1891:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greenpoint.tar.xz
Source1892:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greenpoint.doc.tar.xz
Source1893:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grotesq.tar.xz
Source1894:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grotesq.doc.tar.xz
Source2214:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gamebook.tar.xz
Source2215:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gamebook.doc.tar.xz
Source2217:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/go.tar.xz
Source2218:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/go.doc.tar.xz
Source2287:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gates.tar.xz
Source2288:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gates.doc.tar.xz
Source2348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/genmisc.tar.xz
Source2398:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gb4e.tar.xz
Source2399:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gb4e.doc.tar.xz
Source2400:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmverse.tar.xz
Source2401:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmverse.doc.tar.xz
Source2495:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ghab.tar.xz
Source2496:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ghab.doc.tar.xz
Source2550:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gost.tar.xz
Source2551:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gost.doc.tar.xz
Source2616:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gentle.doc.tar.xz
Source2617:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/guide-to-latex.doc.tar.xz
Source2752:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/geometry-de.doc.tar.xz
Source2753:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/german.tar.xz
Source2754:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/german.doc.tar.xz
Source2756:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/germbib.tar.xz
Source2757:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/germbib.doc.tar.xz
Source2758:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/germkorr.tar.xz
Source2759:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/germkorr.doc.tar.xz
Source2797:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsbaskerville.tar.xz
Source2798:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsbaskerville.doc.tar.xz
Source2799:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsporson.tar.xz
Source2800:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsporson.doc.tar.xz
Source2801:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greek-fontenc.tar.xz
Source2802:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greek-fontenc.doc.tar.xz
Source2803:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greek-inputenc.tar.xz
Source2804:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greek-inputenc.doc.tar.xz
Source2805:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greekdates.tar.xz
Source2806:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greekdates.doc.tar.xz
Source2808:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greektex.tar.xz
Source2809:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greektex.doc.tar.xz
Source2949:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gustlib.tar.xz
Source2950:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gustlib.doc.tar.xz
Source2951:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gustprog.doc.tar.xz
Source3158:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/genealogytree.tar.xz
Source3159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/genealogytree.doc.tar.xz
Source3162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gincltex.tar.xz
Source3163:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gincltex.doc.tar.xz
Source3165:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gnuplottex.tar.xz
Source3166:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gnuplottex.doc.tar.xz
Source3168:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gradientframe.tar.xz
Source3169:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gradientframe.doc.tar.xz
Source3171:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grafcet.tar.xz
Source3172:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grafcet.doc.tar.xz
Source3173:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphviz.tar.xz
Source3174:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphviz.doc.tar.xz
Source4129:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/g-brief.tar.xz
Source4130:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/g-brief.doc.tar.xz
Source4132:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gauss.tar.xz
Source4133:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gauss.doc.tar.xz
Source4134:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gcard.tar.xz
Source4135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gcard.doc.tar.xz
Source4136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gcite.tar.xz
Source4137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gcite.doc.tar.xz
Source4139:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gender.tar.xz
Source4140:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gender.doc.tar.xz
Source4142:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/genmpage.tar.xz
Source4143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/genmpage.doc.tar.xz
Source4145:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/getfiledate.tar.xz
Source4146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/getfiledate.doc.tar.xz
Source4147:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ginpenc.tar.xz
Source4148:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ginpenc.doc.tar.xz
Source4150:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gitinfo.tar.xz
Source4151:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gitinfo.doc.tar.xz
Source4152:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gitinfo2.tar.xz
Source4153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gitinfo2.doc.tar.xz
Source4154:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gloss.tar.xz
Source4155:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gloss.doc.tar.xz
Source4159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-danish.tar.xz
Source4160:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-danish.doc.tar.xz
Source4162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-dutch.tar.xz
Source4163:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-dutch.doc.tar.xz
Source4165:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-english.tar.xz
Source4166:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-english.doc.tar.xz
Source4168:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-french.tar.xz
Source4169:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-french.doc.tar.xz
Source4171:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-german.tar.xz
Source4172:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-german.doc.tar.xz
Source4174:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-irish.tar.xz
Source4175:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-irish.doc.tar.xz
Source4177:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-italian.tar.xz
Source4178:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-italian.doc.tar.xz
Source4180:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-magyar.tar.xz
Source4181:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-magyar.doc.tar.xz
Source4183:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-polish.tar.xz
Source4184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-polish.doc.tar.xz
Source4186:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-portuges.tar.xz
Source4187:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-portuges.doc.tar.xz
Source4189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-serbian.tar.xz
Source4190:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-serbian.doc.tar.xz
Source4192:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-spanish.tar.xz
Source4193:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-spanish.doc.tar.xz
Source4195:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmdoc.tar.xz
Source4196:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmdoc.doc.tar.xz
Source4197:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmdoc-enhance.tar.xz
Source4198:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmdoc-enhance.doc.tar.xz
Source4200:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmiflink.tar.xz
Source4201:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmiflink.doc.tar.xz
Source4202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmutils.tar.xz
Source4203:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmutils.doc.tar.xz
Source4204:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmverb.tar.xz
Source4205:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmverb.doc.tar.xz
Source4206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphbox.tar.xz
Source4207:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphbox.doc.tar.xz
Source4209:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphicx-psmin.tar.xz
Source4210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphicx-psmin.doc.tar.xz
Source4212:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphicxbox.tar.xz
Source4213:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphicxbox.doc.tar.xz
Source4215:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grfpaste.tar.xz
Source4216:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grfpaste.doc.tar.xz
Source4217:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grid.tar.xz
Source4218:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grid.doc.tar.xz
Source4220:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grid-system.tar.xz
Source4221:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grid-system.doc.tar.xz
Source4222:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gridset.tar.xz
Source4223:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gridset.doc.tar.xz
Source4225:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gtl.tar.xz
Source4226:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gtl.doc.tar.xz
Source4228:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/guitlogo.tar.xz
Source4229:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/guitlogo.doc.tar.xz
Source5847:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grundgesetze.tar.xz
Source5848:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grundgesetze.doc.tar.xz
Source5968:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/garrigues.tar.xz
Source5969:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/garrigues.doc.tar.xz
Source5970:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmp.tar.xz
Source5971:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gmp.doc.tar.xz
Source6026:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gchords.tar.xz
Source6027:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gchords.doc.tar.xz
Source6028:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gtrcrd.tar.xz
Source6029:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gtrcrd.doc.tar.xz
Source6030:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/guitar.tar.xz
Source6031:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/guitar.doc.tar.xz
Source6033:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/guitarchordschemes.tar.xz
Source6034:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/guitarchordschemes.doc.tar.xz
Source6084:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/getoptk.tar.xz
Source6085:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/getoptk.doc.tar.xz
Source6086:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfnotation.tar.xz
Source6087:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfnotation.doc.tar.xz
Source6088:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphics-pln.tar.xz
Source6089:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphics-pln.doc.tar.xz
Source6387:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gaceta.tar.xz
Source6388:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gaceta.doc.tar.xz
Source6389:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gatech-thesis.tar.xz
Source6390:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gatech-thesis.doc.tar.xz
Source6391:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gsemthesis.tar.xz
Source6392:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gsemthesis.doc.tar.xz
Source6394:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gzt.tar.xz
Source6395:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gzt.doc.tar.xz
Source6666:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/galois.tar.xz
Source6667:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/galois.doc.tar.xz
Source6669:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gastex.tar.xz
Source6670:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gastex.doc.tar.xz
Source6671:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gene-logic.tar.xz
Source6672:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gene-logic.doc.tar.xz
Source6673:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ghsystem.tar.xz
Source6674:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ghsystem.doc.tar.xz
Source6675:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gu.tar.xz
Source6676:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gu.doc.tar.xz
Source7348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/getitems.tar.xz
Source7349:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/getitems.doc.tar.xz
Source7351:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gitlog.tar.xz
Source7352:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gitlog.doc.tar.xz
Source7353:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-extra.tar.xz
Source7354:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-extra.doc.tar.xz
Source7356:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gloss-occitan.tar.xz
Source7357:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gloss-occitan.doc.tar.xz
Source7359:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gobble.tar.xz
Source7360:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gobble.doc.tar.xz
Source7362:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gradstudentresume.tar.xz
Source7363:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gradstudentresume.doc.tar.xz
Source7364:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphics-cfg.tar.xz
Source7365:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphics-cfg.doc.tar.xz
Source7366:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greektonoi.tar.xz
Source7367:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/greektonoi.doc.tar.xz
Source7608:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphics-def.tar.xz
Source7761:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gitfile-info.tar.xz
Source7762:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gitfile-info.doc.tar.xz
Source7763:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gofonts.tar.xz
Source7764:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gofonts.doc.tar.xz
Source7765:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grant.tar.xz
Source7766:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grant.doc.tar.xz
Source7767:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grayhints.tar.xz
Source7768:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/grayhints.doc.tar.xz
Source7769:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gtrlib-largetrees.tar.xz
Source7770:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gtrlib-largetrees.doc.tar.xz
Source8152:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gatherenum.tar.xz
Source8153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gatherenum.doc.tar.xz
Source8154:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gbt7714.tar.xz
Source8155:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gbt7714.doc.tar.xz
Source8156:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gentombow.tar.xz
Source8157:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gentombow.doc.tar.xz
Source8158:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsneohellenicmath.tar.xz
Source8159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gfsneohellenicmath.doc.tar.xz
Source8160:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-finnish.tar.xz
Source8161:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries-finnish.doc.tar.xz
Source8162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gotoh.tar.xz
Source8163:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gotoh.doc.tar.xz
Source8164:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graph35.tar.xz
Source8165:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graph35.doc.tar.xz
Source8166:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphicxpsd.tar.xz
Source8167:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/graphicxpsd.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-garuda-c90
Provides:       tex-garuda-c90 = %{tl_version}
License:        LPPL
Summary:        TeX support (from CJK) for the garuda font
Version:        svn37677.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-fonts-tlwg
Provides:       tex(garuda-c90.map) = %{tl_version}, tex(fgdb8z.tfm) = %{tl_version}
Provides:       tex(fgdbo8z.tfm) = %{tl_version}, tex(fgdo8z.tfm) = %{tl_version}
Provides:       tex(fgdr8z.tfm) = %{tl_version}

%description -n texlive-garuda-c90
garuda-c90 package

%package -n texlive-geometry
Provides:       tex-geometry = %{tl_version}
License:        LPPL
Summary:        Flexible and complete interface to document dimensions
Version:        svn47638
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty), tex(ifpdf.sty), tex(ifvtex.sty), tex(ifxetex.sty)
Requires:       tex(atbegshi.sty)
Provides:       tex(geometry.sty) = %{tl_version}

%description -n texlive-geometry
The package provides an easy and flexible user interface to
customize page layout, implementing auto-centering and auto-
balancing mechanisms so that the users have only to give the
least description for the page layout. For example, if you want
to set each margin 2cm without header space, what you need is
just \usepackage[margin=2cm,nohead]{geometry}. The package
knows about all the standard paper sizes, so that the user need
not know what the nominal 'real' dimensions of the paper are,
just its standard name (such as a4, letter, etc.). An important
feature is the package's ability to communicate the paper size
it's set up to the output (whether via DVI \specials or via
direct interaction with PDF(La)TeX).

%package -n texlive-geometry-doc
Summary:        Documentation for geometry
Version:        svn47638
Provides:       tex-geometry-doc
AutoReqProv:    No

%description -n texlive-geometry-doc
Documentation for geometry

%package -n texlive-graphics
Provides:       tex-graphics = %{tl_version}
License:        LPPL 1.3
Summary:        Standard LaTeX graphics
Version:        svn47350
Provides:       texlive-rotating = %{epoch}:svn16832.2.16b.obsolete
Obsoletes:      texlive-rotating <= 6:svn16832.2.16b
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-graphics-cfg, tex(trig.sty)
Provides:       tex(color.sty) = %{tl_version}, tex(dvipdf.def) = %{tl_version}
Provides:       tex(dvipsnam.def) = %{tl_version}, tex(dvipsone.def) = %{tl_version}
Provides:       tex(dviwin.def) = %{tl_version}, tex(emtex.def) = %{tl_version}
Provides:       tex(epsfig.sty) = %{tl_version}, tex(graphics.sty) = %{tl_version}
Provides:       tex(graphicx.sty) = %{tl_version}, tex(keyval.sty) = %{tl_version}
Provides:       tex(lscape.sty) = %{tl_version}, tex(pctex32.def) = %{tl_version}
Provides:       tex(pctexhp.def) = %{tl_version}, tex(pctexps.def) = %{tl_version}
Provides:       tex(pctexwin.def) = %{tl_version}, tex(rotating.sty) = %{tl_version}
Provides:       tex(tcidvi.def) = %{tl_version}, tex(trig.sty) = %{tl_version}
Provides:       tex(truetex.def) = %{tl_version}

%description -n texlive-graphics
The package was designed to accommodate all needs for inclusion
of graphics in LaTeX documents, replacing many earlier packages
used in LaTeX 2.09. The package aims to give a consistent
interface to including the file types that are understood in
your output, by use of 'printer drivers' (now known, simply, as
'drivers'). The distribtion of the package contains several
drivers, but others (for example, pdfTeX) are distributed
separately. The package also offers several means of
manipulating graphics in the course of inserting them into a
document (for example, rotation and scaling). For extended
documentation see epslatex. The package is part of the graphics
bundle, which is one of the collections in the LaTeX 'required'
set of packages.

%package -n texlive-graphics-doc
Summary:        Documentation for graphics
Version:        svn47350
Provides:       texlive-rotating-doc = svn16832.2.16b.obsolete
Obsoletes:      texlive-rotating-doc <= svn16832.2.16b
Provides:       tex-graphics-doc
AutoReqProv:    No

%description -n texlive-graphics-doc
Documentation for graphics

%package -n texlive-geschichtsfrkl
Provides:       tex-geschichtsfrkl = %{tl_version}
License:        LPPL
Summary:        BibLaTeX style for historians
Version:        svn42121
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(standard.bbx)
Provides:       tex(geschichtsfrkl.bbx) = %{tl_version}, tex(geschichtsfrkl.cbx) = %{tl_version}

%description -n texlive-geschichtsfrkl
The package provides a BibLaTeX style, (mostly) meeting the
requirements of the History Faculty of the University of
Freiburg (Germany).

%package -n texlive-geschichtsfrkl-doc
Summary:        Documentation for geschichtsfrkl
Version:        svn42121
Provides:       tex-geschichtsfrkl-doc
AutoReqProv:    No

%description -n texlive-geschichtsfrkl-doc
Documentation for geschichtsfrkl

%package -n texlive-genealogy
Provides:       tex-genealogy = %{tl_version}
License:        LPPL
Summary:        A compilation genealogy font
Version:        svn25112.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(drgen10.tfm) = %{tl_version}

%description -n texlive-genealogy
A simple compilation of the genealogical symbols found in the
wasy and gen fonts, adding the male and female symbols to
Knuth's 'gen' font, and so avoiding loading two fonts when you
need only genealogical symbols. The font is distributed as
Metafont source.

%package -n texlive-genealogy-doc
Summary:        Documentation for genealogy
Version:        svn25112.0

Provides:       tex-genealogy-doc
AutoReqProv:    No

%description -n texlive-genealogy-doc
Documentation for genealogy

%package -n texlive-gentium-tug
Provides:       tex-gentium-tug = %{tl_version}
License:        MIT and OFL
Summary:        Gentium fonts (in two formats) and support files
Version:        svn37378.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty)
Provides:       tex(gentium-agr.enc) = %{tl_version}, tex(gentium-ec-sc.enc) = %{tl_version}
Provides:       tex(gentium-ec-ttf-sc.enc) = %{tl_version}
Provides:       tex(gentium-ec-ttf.enc) = %{tl_version}, tex(gentium-ec.enc) = %{tl_version}
Provides:       tex(gentium-l7x-sc.enc) = %{tl_version}, tex(gentium-l7x.enc) = %{tl_version}
Provides:       tex(gentium-lgr.enc) = %{tl_version}, tex(gentium-ot1-sc.enc) = %{tl_version}
Provides:       tex(gentium-ot1.enc) = %{tl_version}, tex(gentium-qx-sc.enc) = %{tl_version}
Provides:       tex(gentium-qx.enc) = %{tl_version}, tex(gentium-t2a-sc.enc) = %{tl_version}
Provides:       tex(gentium-t2a.enc) = %{tl_version}, tex(gentium-t2b-sc.enc) = %{tl_version}
Provides:       tex(gentium-t2b.enc) = %{tl_version}, tex(gentium-t2c-sc.enc) = %{tl_version}
Provides:       tex(gentium-t2c.enc) = %{tl_version}, tex(gentium-t5-sc.enc) = %{tl_version}
Provides:       tex(gentium-t5-ttf.enc) = %{tl_version}, tex(gentium-t5.enc) = %{tl_version}
Provides:       tex(gentium-texnansi-sc.enc) = %{tl_version}
Provides:       tex(gentium-texnansi.enc) = %{tl_version}
Provides:       tex(gentium-ts1.enc) = %{tl_version}, tex(gentium-x2-sc.enc) = %{tl_version}
Provides:       tex(gentium-x2.enc) = %{tl_version}, tex(gentium-type1.map) = %{tl_version}
Provides:       tex(gentium-agr.map) = %{tl_version}, tex(gentium-ec.map) = %{tl_version}
Provides:       tex(gentium-l7x.map) = %{tl_version}, tex(gentium-lgr.map) = %{tl_version}
Provides:       tex(gentium-ot1.map) = %{tl_version}, tex(gentium-qx.map) = %{tl_version}
Provides:       tex(gentium-t2a.map) = %{tl_version}, tex(gentium-t2b.map) = %{tl_version}
Provides:       tex(gentium-t2c.map) = %{tl_version}, tex(gentium-t5.map) = %{tl_version}
Provides:       tex(gentium-texnansi.map) = %{tl_version}
Provides:       tex(gentium-truetype.map) = %{tl_version}
Provides:       tex(gentium-ts1.map) = %{tl_version}, tex(gentium-x2.map) = %{tl_version}
Provides:       tex(agr-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(agr-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(ec-gentiumbasic-bold.tfm) = %{tl_version}
Provides:       tex(ec-gentiumbasic-bolditalic.tfm) = %{tl_version}
Provides:       tex(ec-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(ec-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(ec-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(ec-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(l7x-gentiumbasic-bold.tfm) = %{tl_version}
Provides:       tex(l7x-gentiumbasic-bolditalic.tfm) = %{tl_version}
Provides:       tex(l7x-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(l7x-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(l7x-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(l7x-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(lgr-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(lgr-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(ot1-gentiumbasic-bold.tfm) = %{tl_version}
Provides:       tex(ot1-gentiumbasic-bolditalic.tfm) = %{tl_version}
Provides:       tex(ot1-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(ot1-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(ot1-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(ot1-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(qx-gentiumbasic-bold.tfm) = %{tl_version}
Provides:       tex(qx-gentiumbasic-bolditalic.tfm) = %{tl_version}
Provides:       tex(qx-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(qx-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(qx-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(qx-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(t2a-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(t2a-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(t2a-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(t2a-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(t2b-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(t2b-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(t2b-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(t2b-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(t2c-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(t2c-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(t2c-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(t2c-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(t5-gentiumbasic-bold.tfm) = %{tl_version}
Provides:       tex(t5-gentiumbasic-bolditalic.tfm) = %{tl_version}
Provides:       tex(t5-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(t5-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(t5-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(t5-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(texnansi-gentiumbasic-bold.tfm) = %{tl_version}
Provides:       tex(texnansi-gentiumbasic-bolditalic.tfm) = %{tl_version}
Provides:       tex(texnansi-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(texnansi-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(texnansi-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(ts1-gentiumbasic-bold.tfm) = %{tl_version}
Provides:       tex(ts1-gentiumbasic-bolditalic.tfm) = %{tl_version}
Provides:       tex(ts1-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(ts1-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(x2-gentiumplus-italic-sc.tfm) = %{tl_version}
Provides:       tex(x2-gentiumplus-italic.tfm) = %{tl_version}
Provides:       tex(x2-gentiumplus-regular-sc.tfm) = %{tl_version}
Provides:       tex(x2-gentiumplus-regular.tfm) = %{tl_version}
Provides:       tex(GenBasB.ttf) = %{tl_version}, tex(GenBasBI.ttf) = %{tl_version}
Provides:       tex(GenBasI.ttf) = %{tl_version}, tex(GenBasR.ttf) = %{tl_version}
Provides:       tex(GenBkBasB.ttf) = %{tl_version}, tex(GenBkBasBI.ttf) = %{tl_version}
Provides:       tex(GenBkBasI.ttf) = %{tl_version}, tex(GenBkBasR.ttf) = %{tl_version}
Provides:       tex(Gentium-I.ttf) = %{tl_version}, tex(Gentium-R.ttf) = %{tl_version}
Provides:       tex(GentiumAlt-I.ttf) = %{tl_version}, tex(GentiumAlt-R.ttf) = %{tl_version}
Provides:       tex(GentiumPlus-I.ttf) = %{tl_version}, tex(GentiumPlus-R.ttf) = %{tl_version}
Provides:       tex(GentiumPlusCompact-I.ttf) = %{tl_version}
Provides:       tex(GentiumPlusCompact-R.ttf) = %{tl_version}
Provides:       tex(GenBasB.pfb) = %{tl_version}, tex(GenBasBI.pfb) = %{tl_version}
Provides:       tex(GentiumPlus-I.pfb) = %{tl_version}, tex(GentiumPlus-R.pfb) = %{tl_version}
Provides:       tex(gentium.sty) = %{tl_version}, tex(l7xgentium.fd) = %{tl_version}
Provides:       tex(lgrgentium.fd) = %{tl_version}, tex(ly1gentium.fd) = %{tl_version}
Provides:       tex(ot1gentium.fd) = %{tl_version}, tex(qxgentium.fd) = %{tl_version}
Provides:       tex(t1gentium.fd) = %{tl_version}, tex(t2agentium.fd) = %{tl_version}
Provides:       tex(t2bgentium.fd) = %{tl_version}, tex(t2cgentium.fd) = %{tl_version}
Provides:       tex(t5gentium.fd) = %{tl_version}, tex(ts1gentium.fd) = %{tl_version}
Provides:       tex(x2gentium.fd) = %{tl_version}

%description -n texlive-gentium-tug
Gentium is a typeface family designed to enable the diverse
ethnic groups around the world who use the Latin, Cyrillic and
Greek scripts to produce readable, high-quality publications.
It supports a wide range of Latin- and Cyrillic-based
alphabets. The package consists of: The original (unaltered)
GentiumPlus, GentiumBook, and other Gentium-family fonts in
TrueType format, as developed by SIL and released under the OFL
(see OFL.txt and OFL-FAQ.txt); Converted fonts in PostScript
Type 1 format, released under the same terms. These incorporate
the name "Gentium" by permission of SIL given to the TeX Users
Group; ConTeXt, LaTeX and other supporting files; TeX-related
documentation, and the SIL documentation and other files.

%package -n texlive-gentium-tug-doc
Summary:        Documentation for gentium-tug
Version:        svn37378.1.1

Provides:       tex-gentium-tug-doc
AutoReqProv:    No

%description -n texlive-gentium-tug-doc
Documentation for gentium-tug

%package -n texlive-gfsartemisia
Provides:       tex-gfsartemisia = %{tl_version}
License:        LPPL
Summary:        A modern Greek font design
Version:        svn19469.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(euler.sty), tex(txfonts.sty)
Provides:       tex(artemisia.enc) = %{tl_version}, tex(artemisiadenomnums.enc) = %{tl_version}
Provides:       tex(artemisiaec.enc) = %{tl_version}, tex(artemisiaecsc.enc) = %{tl_version}
Provides:       tex(artemisiael.enc) = %{tl_version}, tex(artemisiaelsc.enc) = %{tl_version}
Provides:       tex(artemisiamath.enc) = %{tl_version}, tex(artemisianumnums.enc) = %{tl_version}
Provides:       tex(artemisiasc.enc) = %{tl_version}, tex(artemisiatabnums.enc) = %{tl_version}
Provides:       tex(gfsartemisia.map) = %{tl_version}, tex(GFSArtemisia.otf) = %{tl_version}
Provides:       tex(GFSArtemisiaBold.otf) = %{tl_version}
Provides:       tex(GFSArtemisiaBoldIt.otf) = %{tl_version}
Provides:       tex(GFSArtemisiaIt.otf) = %{tl_version}, tex(artemisiab8a.tfm) = %{tl_version}
Provides:       tex(artemisiab8r.tfm) = %{tl_version}, tex(artemisiab9a.tfm) = %{tl_version}
Provides:       tex(artemisiab9r.tfm) = %{tl_version}, tex(artemisiabi8a.tfm) = %{tl_version}
Provides:       tex(artemisiabi8r.tfm) = %{tl_version}, tex(artemisiabi9a.tfm) = %{tl_version}
Provides:       tex(artemisiabi9r.tfm) = %{tl_version}, tex(artemisiabo8a.tfm) = %{tl_version}
Provides:       tex(artemisiabo8r.tfm) = %{tl_version}, tex(artemisiabo9a.tfm) = %{tl_version}
Provides:       tex(artemisiabo9r.tfm) = %{tl_version}, tex(artemisiadenomnums8a.tfm) = %{tl_version}
Provides:       tex(artemisiadenomnums8r.tfm) = %{tl_version}
Provides:       tex(artemisiai8a.tfm) = %{tl_version}, tex(artemisiai8r.tfm) = %{tl_version}
Provides:       tex(artemisiai9a.tfm) = %{tl_version}, tex(artemisiai9r.tfm) = %{tl_version}
Provides:       tex(artemisiamath8a.tfm) = %{tl_version}
Provides:       tex(artemisiamath8r.tfm) = %{tl_version}
Provides:       tex(artemisianumnums8a.tfm) = %{tl_version}
Provides:       tex(artemisianumnums8r.tfm) = %{tl_version}
Provides:       tex(artemisiao8a.tfm) = %{tl_version}, tex(artemisiao8r.tfm) = %{tl_version}
Provides:       tex(artemisiao9a.tfm) = %{tl_version}, tex(artemisiao9r.tfm) = %{tl_version}
Provides:       tex(artemisiarg8a.tfm) = %{tl_version}, tex(artemisiarg8r.tfm) = %{tl_version}
Provides:       tex(artemisiarg9a.tfm) = %{tl_version}, tex(artemisiarg9r.tfm) = %{tl_version}
Provides:       tex(artemisiasc8a.tfm) = %{tl_version}, tex(artemisiasc8r.tfm) = %{tl_version}
Provides:       tex(artemisiasc9a.tfm) = %{tl_version}, tex(artemisiasc9r.tfm) = %{tl_version}
Provides:       tex(artemisiasco8a.tfm) = %{tl_version}, tex(artemisiasco8r.tfm) = %{tl_version}
Provides:       tex(artemisiasco9a.tfm) = %{tl_version}, tex(artemisiasco9r.tfm) = %{tl_version}
Provides:       tex(artemisiatabnums8a.tfm) = %{tl_version}
Provides:       tex(artemisiatabnums8r.tfm) = %{tl_version}
Provides:       tex(gartemisiab6a.tfm) = %{tl_version}, tex(gartemisiab6r.tfm) = %{tl_version}
Provides:       tex(gartemisiabi6a.tfm) = %{tl_version}, tex(gartemisiabi6r.tfm) = %{tl_version}
Provides:       tex(gartemisiabo6a.tfm) = %{tl_version}, tex(gartemisiabo6r.tfm) = %{tl_version}
Provides:       tex(gartemisiai6a.tfm) = %{tl_version}, tex(gartemisiai6r.tfm) = %{tl_version}
Provides:       tex(gartemisiao6a.tfm) = %{tl_version}, tex(gartemisiao6r.tfm) = %{tl_version}
Provides:       tex(gartemisiarg6a.tfm) = %{tl_version}, tex(gartemisiarg6r.tfm) = %{tl_version}
Provides:       tex(gartemisiasc6a.tfm) = %{tl_version}, tex(gartemisiasc6r.tfm) = %{tl_version}
Provides:       tex(gartemisiasco6a.tfm) = %{tl_version}
Provides:       tex(gartemisiasco6r.tfm) = %{tl_version}
Provides:       tex(GFSArtemisia-Bold.pfb) = %{tl_version}
Provides:       tex(GFSArtemisia-BoldItalic.pfb) = %{tl_version}
Provides:       tex(GFSArtemisia-Italic.pfb) = %{tl_version}
Provides:       tex(GFSArtemisia-Regular.pfb) = %{tl_version}
Provides:       tex(artemisiab8a.vf) = %{tl_version}, tex(artemisiab9a.vf) = %{tl_version}
Provides:       tex(artemisiabi8a.vf) = %{tl_version}, tex(artemisiabi9a.vf) = %{tl_version}
Provides:       tex(artemisiabo8a.vf) = %{tl_version}, tex(artemisiabo9a.vf) = %{tl_version}
Provides:       tex(artemisiadenomnums8a.vf) = %{tl_version}
Provides:       tex(artemisiai8a.vf) = %{tl_version}, tex(artemisiai9a.vf) = %{tl_version}
Provides:       tex(artemisiamath8a.vf) = %{tl_version}, tex(artemisianumnums8a.vf) = %{tl_version}
Provides:       tex(artemisiao8a.vf) = %{tl_version}, tex(artemisiao9a.vf) = %{tl_version}
Provides:       tex(artemisiarg8a.vf) = %{tl_version}, tex(artemisiarg9a.vf) = %{tl_version}
Provides:       tex(artemisiasc8a.vf) = %{tl_version}, tex(artemisiasc9a.vf) = %{tl_version}
Provides:       tex(artemisiasco8a.vf) = %{tl_version}, tex(artemisiasco9a.vf) = %{tl_version}
Provides:       tex(artemisiatabnums8a.vf) = %{tl_version}
Provides:       tex(gartemisiab6a.vf) = %{tl_version}, tex(gartemisiabi6a.vf) = %{tl_version}
Provides:       tex(gartemisiabo6a.vf) = %{tl_version}, tex(gartemisiai6a.vf) = %{tl_version}
Provides:       tex(gartemisiao6a.vf) = %{tl_version}, tex(gartemisiarg6a.vf) = %{tl_version}
Provides:       tex(gartemisiasc6a.vf) = %{tl_version}, tex(gartemisiasco6a.vf) = %{tl_version}
Provides:       tex(gfsartemisia-euler.sty) = %{tl_version}
Provides:       tex(gfsartemisia.sty) = %{tl_version}, tex(lgrartemisia.fd) = %{tl_version}
Provides:       tex(lgrartemisiaeuler.fd) = %{tl_version}
Provides:       tex(ot1artemisia.fd) = %{tl_version}, tex(ot1artemisiaeuler.fd) = %{tl_version}
Provides:       tex(t1artemisia.fd) = %{tl_version}, tex(t1artemisiaeuler.fd) = %{tl_version}
Provides:       tex(uartemisiaeulernums.fd) = %{tl_version}
Provides:       tex(uartemisianums.fd) = %{tl_version}

%description -n texlive-gfsartemisia
GFS Artemisia is a relatively modern font, designed as a
'general purpose' font in the same sense as Times is nowadays
treated. The present version has been provided by the Greek
Font Society. The font supports the Greek and Latin alphabets.
LaTeX support is provided, using the OT1, T1 and LGR encodings.

%package -n texlive-gfsartemisia-doc
Summary:        Documentation for gfsartemisia
Version:        svn19469.1.0

Provides:       tex-gfsartemisia-doc
AutoReqProv:    No

%description -n texlive-gfsartemisia-doc
Documentation for gfsartemisia

%package -n texlive-gfsbodoni
Provides:       tex-gfsbodoni = %{tl_version}
License:        OFL
Summary:        A Greek and Latin font based on Bodoni
Version:        svn28484.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(bodoni.enc) = %{tl_version}, tex(bodonidenomnums.enc) = %{tl_version}
Provides:       tex(bodoniec.enc) = %{tl_version}, tex(bodoniecsc.enc) = %{tl_version}
Provides:       tex(bodoniel.enc) = %{tl_version}, tex(bodonielsc.enc) = %{tl_version}
Provides:       tex(bodoninumnums.enc) = %{tl_version}, tex(bodonisc.enc) = %{tl_version}
Provides:       tex(bodonitabnums.enc) = %{tl_version}, tex(gfsbodoni.map) = %{tl_version}
Provides:       tex(GFSBodoni.otf) = %{tl_version}, tex(GFSBodoniBold.otf) = %{tl_version}
Provides:       tex(GFSBodoniBoldIt.otf) = %{tl_version}
Provides:       tex(GFSBodoniIt.otf) = %{tl_version}, tex(bodonib8a.tfm) = %{tl_version}
Provides:       tex(bodonib8r.tfm) = %{tl_version}, tex(bodonib9a.tfm) = %{tl_version}
Provides:       tex(bodonib9r.tfm) = %{tl_version}, tex(bodonibi8a.tfm) = %{tl_version}
Provides:       tex(bodonibi8r.tfm) = %{tl_version}, tex(bodonibi9a.tfm) = %{tl_version}
Provides:       tex(bodonibi9r.tfm) = %{tl_version}, tex(bodonibo8a.tfm) = %{tl_version}
Provides:       tex(bodonibo8r.tfm) = %{tl_version}, tex(bodonibo9a.tfm) = %{tl_version}
Provides:       tex(bodonibo9r.tfm) = %{tl_version}, tex(bodonidenomnums8a.tfm) = %{tl_version}
Provides:       tex(bodonidenomnums8r.tfm) = %{tl_version}
Provides:       tex(bodonii8a.tfm) = %{tl_version}, tex(bodonii8r.tfm) = %{tl_version}
Provides:       tex(bodonii9a.tfm) = %{tl_version}, tex(bodonii9r.tfm) = %{tl_version}
Provides:       tex(bodoninumnums8a.tfm) = %{tl_version}
Provides:       tex(bodoninumnums8r.tfm) = %{tl_version}
Provides:       tex(bodonio8a.tfm) = %{tl_version}, tex(bodonio8r.tfm) = %{tl_version}
Provides:       tex(bodonio9a.tfm) = %{tl_version}, tex(bodonio9r.tfm) = %{tl_version}
Provides:       tex(bodonirg8a.tfm) = %{tl_version}, tex(bodonirg8r.tfm) = %{tl_version}
Provides:       tex(bodonirg9a.tfm) = %{tl_version}, tex(bodonirg9r.tfm) = %{tl_version}
Provides:       tex(bodonisc8a.tfm) = %{tl_version}, tex(bodonisc8r.tfm) = %{tl_version}
Provides:       tex(bodonisc9a.tfm) = %{tl_version}, tex(bodonisc9r.tfm) = %{tl_version}
Provides:       tex(bodonisco8a.tfm) = %{tl_version}, tex(bodonisco8r.tfm) = %{tl_version}
Provides:       tex(bodonisco9a.tfm) = %{tl_version}, tex(bodonisco9r.tfm) = %{tl_version}
Provides:       tex(bodonitabnums8a.tfm) = %{tl_version}
Provides:       tex(bodonitabnums8r.tfm) = %{tl_version}
Provides:       tex(gbodonib6a.tfm) = %{tl_version}, tex(gbodonib6r.tfm) = %{tl_version}
Provides:       tex(gbodonibi6a.tfm) = %{tl_version}, tex(gbodonibi6r.tfm) = %{tl_version}
Provides:       tex(gbodonibo6a.tfm) = %{tl_version}, tex(gbodonibo6r.tfm) = %{tl_version}
Provides:       tex(gbodonii6a.tfm) = %{tl_version}, tex(gbodonii6r.tfm) = %{tl_version}
Provides:       tex(gbodonio6a.tfm) = %{tl_version}, tex(gbodonio6r.tfm) = %{tl_version}
Provides:       tex(gbodonio9a.tfm) = %{tl_version}, tex(gbodonirg6a.tfm) = %{tl_version}
Provides:       tex(gbodonirg6r.tfm) = %{tl_version}, tex(gbodonisc6a.tfm) = %{tl_version}
Provides:       tex(gbodonisc6r.tfm) = %{tl_version}, tex(gbodonisco6a.tfm) = %{tl_version}
Provides:       tex(gbodonisco6r.tfm) = %{tl_version}, tex(GFSBodoni-Bold.pfb) = %{tl_version}
Provides:       tex(GFSBodoni-BoldItalic.pfb) = %{tl_version}
Provides:       tex(GFSBodoni-Italic.pfb) = %{tl_version}
Provides:       tex(GFSBodoni-Regular.pfb) = %{tl_version}
Provides:       tex(bodonib8a.vf) = %{tl_version}, tex(bodonib9a.vf) = %{tl_version}
Provides:       tex(bodonibi8a.vf) = %{tl_version}, tex(bodonibi9a.vf) = %{tl_version}
Provides:       tex(bodonibo8a.vf) = %{tl_version}, tex(bodonibo9a.vf) = %{tl_version}
Provides:       tex(bodonidenomnums8a.vf) = %{tl_version}
Provides:       tex(bodonii8a.vf) = %{tl_version}, tex(bodonii9a.vf) = %{tl_version}
Provides:       tex(bodoninumnums8a.vf) = %{tl_version}, tex(bodonio8a.vf) = %{tl_version}
Provides:       tex(bodonio9a.vf) = %{tl_version}, tex(bodonirg8a.vf) = %{tl_version}
Provides:       tex(bodonirg9a.vf) = %{tl_version}, tex(bodonisc8a.vf) = %{tl_version}
Provides:       tex(bodonisc9a.vf) = %{tl_version}, tex(bodonisco8a.vf) = %{tl_version}
Provides:       tex(bodonisco9a.vf) = %{tl_version}, tex(bodonitabnums8a.vf) = %{tl_version}
Provides:       tex(gbodonib6a.vf) = %{tl_version}, tex(gbodonibi6a.vf) = %{tl_version}
Provides:       tex(gbodonibo6a.vf) = %{tl_version}, tex(gbodonii6a.vf) = %{tl_version}
Provides:       tex(gbodonio6a.vf) = %{tl_version}, tex(gbodonio9a.vf) = %{tl_version}
Provides:       tex(gbodonirg6a.vf) = %{tl_version}, tex(gbodonisc6a.vf) = %{tl_version}
Provides:       tex(gbodonisco6a.vf) = %{tl_version}, tex(gfsbodoni.sty) = %{tl_version}
Provides:       tex(lgrbodoni.fd) = %{tl_version}, tex(ot1bodoni.fd) = %{tl_version}
Provides:       tex(t1bodoni.fd) = %{tl_version}, tex(ubodoninums.fd) = %{tl_version}

%description -n texlive-gfsbodoni
Bodoni's Greek fonts in the 18th century broke, for the first
time, with the Byzantine cursive tradition of Greek fonts. GFS
Bodoni resurrects his work for general use. The font family
supports both Greek and Latin letters. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings. The
fonts themselves are provided in Adobe Type 1 and OpenType
formats.

%package -n texlive-gfsbodoni-doc
Summary:        Documentation for gfsbodoni
Version:        svn28484.1.01

Provides:       tex-gfsbodoni-doc
AutoReqProv:    No

%description -n texlive-gfsbodoni-doc
Documentation for gfsbodoni

%package -n texlive-gfscomplutum
Provides:       tex-gfscomplutum = %{tl_version}
License:        OFL
Summary:        A Greek font with a long history
Version:        svn19469.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(gpcomplutum.enc) = %{tl_version}, tex(gfscomplutum.map) = %{tl_version}
Provides:       tex(GFSPolyglot.otf) = %{tl_version}, tex(gcomplutum8a.tfm) = %{tl_version}
Provides:       tex(gcomplutum8r.tfm) = %{tl_version}, tex(gcomplutumo8a.tfm) = %{tl_version}
Provides:       tex(gcomplutumo8r.tfm) = %{tl_version}, tex(GFSComplutum-Regular.pfb) = %{tl_version}
Provides:       tex(gcomplutum8a.vf) = %{tl_version}, tex(gcomplutumo8a.vf) = %{tl_version}
Provides:       tex(gfscomplutum.sty) = %{tl_version}, tex(lgrcomplutum.fd) = %{tl_version}

%description -n texlive-gfscomplutum
GFS Complutum derives, via a long development, from a minuscule-
only font cut in the 16th century. An unsatisfactory set of
majuscules were added in the early 20th century, but its author
died before he could complete the revival of the font. The
Greek Font Society has released this version, which has a new
set of majuscules.

%package -n texlive-gfscomplutum-doc
Summary:        Documentation for gfscomplutum
Version:        svn19469.1.0

Provides:       tex-gfscomplutum-doc
AutoReqProv:    No

%description -n texlive-gfscomplutum-doc
Documentation for gfscomplutum

%package -n texlive-gfsdidot
Provides:       tex-gfsdidot = %{tl_version}
License:        LPPL
Summary:        A Greek font based on Didot's work
Version:        svn46310
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(pxfonts.sty)
Provides:       tex(didot.enc) = %{tl_version}, tex(didotdenomnums.enc) = %{tl_version}
Provides:       tex(didotec.enc) = %{tl_version}, tex(didotnumnums.enc) = %{tl_version}
Provides:       tex(didottabnums.enc) = %{tl_version}, tex(didotuecsc.enc) = %{tl_version}
Provides:       tex(didotusc.enc) = %{tl_version}, tex(gfsudidotmath.enc) = %{tl_version}
Provides:       tex(gpdidot.enc) = %{tl_version}, tex(gpdidoti.enc) = %{tl_version}
Provides:       tex(gpdidotusc.enc) = %{tl_version}, tex(gpolga.enc) = %{tl_version}
Provides:       tex(gfsdidot.map) = %{tl_version}, tex(GFSDidot.otf) = %{tl_version}
Provides:       tex(GFSDidotBold.otf) = %{tl_version}, tex(GFSDidotBoldItalic.otf) = %{tl_version}
Provides:       tex(GFSDidotItalic.otf) = %{tl_version}, tex(GFSOlga.otf) = %{tl_version}
Provides:       tex(didotb8a.tfm) = %{tl_version}, tex(didotb8r.tfm) = %{tl_version}
Provides:       tex(didotb9a.tfm) = %{tl_version}, tex(didotb9r.tfm) = %{tl_version}
Provides:       tex(didotbi8a.tfm) = %{tl_version}, tex(didotbi8r.tfm) = %{tl_version}
Provides:       tex(didotbi9a.tfm) = %{tl_version}, tex(didotbi9r.tfm) = %{tl_version}
Provides:       tex(didotbo8a.tfm) = %{tl_version}, tex(didotbo8r.tfm) = %{tl_version}
Provides:       tex(didotbo9a.tfm) = %{tl_version}, tex(didotbo9r.tfm) = %{tl_version}
Provides:       tex(didotdenomnums8a.tfm) = %{tl_version}
Provides:       tex(didotdenomnums8r.tfm) = %{tl_version}
Provides:       tex(didoti8a.tfm) = %{tl_version}, tex(didoti8r.tfm) = %{tl_version}
Provides:       tex(didoti9a.tfm) = %{tl_version}, tex(didoti9r.tfm) = %{tl_version}
Provides:       tex(didotnumnums8a.tfm) = %{tl_version}, tex(didotnumnums8r.tfm) = %{tl_version}
Provides:       tex(didoto8a.tfm) = %{tl_version}, tex(didoto8r.tfm) = %{tl_version}
Provides:       tex(didoto9a.tfm) = %{tl_version}, tex(didoto9r.tfm) = %{tl_version}
Provides:       tex(didotrg8a.tfm) = %{tl_version}, tex(didotrg8r.tfm) = %{tl_version}
Provides:       tex(didotrg9a.tfm) = %{tl_version}, tex(didotrg9r.tfm) = %{tl_version}
Provides:       tex(didotsc8a.tfm) = %{tl_version}, tex(didotsc8r.tfm) = %{tl_version}
Provides:       tex(didotsc9a.tfm) = %{tl_version}, tex(didotsc9r.tfm) = %{tl_version}
Provides:       tex(didotsco8a.tfm) = %{tl_version}, tex(didotsco8r.tfm) = %{tl_version}
Provides:       tex(didotsco9a.tfm) = %{tl_version}, tex(didotsco9r.tfm) = %{tl_version}
Provides:       tex(didottabnums8a.tfm) = %{tl_version}, tex(didottabnums8r.tfm) = %{tl_version}
Provides:       tex(didotui8a.tfm) = %{tl_version}, tex(didotui8r.tfm) = %{tl_version}
Provides:       tex(didotui9a.tfm) = %{tl_version}, tex(didotui9r.tfm) = %{tl_version}
Provides:       tex(gdidotb6a.tfm) = %{tl_version}, tex(gdidotb6r.tfm) = %{tl_version}
Provides:       tex(gdidotbi6a.tfm) = %{tl_version}, tex(gdidotbi6r.tfm) = %{tl_version}
Provides:       tex(gdidoti6a.tfm) = %{tl_version}, tex(gdidoti6r.tfm) = %{tl_version}
Provides:       tex(gdidotrg6a.tfm) = %{tl_version}, tex(gdidotrg6r.tfm) = %{tl_version}
Provides:       tex(gdidotsc6a.tfm) = %{tl_version}, tex(gdidotsc6r.tfm) = %{tl_version}
Provides:       tex(gdidotsco6a.tfm) = %{tl_version}, tex(gdidotsco6r.tfm) = %{tl_version}
Provides:       tex(gfsudidotmath8a.tfm) = %{tl_version}
Provides:       tex(gfsudidotmath8r.tfm) = %{tl_version}
Provides:       tex(golgai6a.tfm) = %{tl_version}, tex(golgai6r.tfm) = %{tl_version}
Provides:       tex(golgaui6a.tfm) = %{tl_version}, tex(golgaui6r.tfm) = %{tl_version}
Provides:       tex(GFSDidot-Bold.pfb) = %{tl_version}, tex(GFSDidot-BoldItalic.pfb) = %{tl_version}
Provides:       tex(GFSDidot-Italic.pfb) = %{tl_version}
Provides:       tex(GFSDidot.pfb) = %{tl_version}, tex(GFSOlga.pfb) = %{tl_version}
Provides:       tex(didotb8a.vf) = %{tl_version}, tex(didotb9a.vf) = %{tl_version}
Provides:       tex(didotbi8a.vf) = %{tl_version}, tex(didotbi9a.vf) = %{tl_version}
Provides:       tex(didotbo8a.vf) = %{tl_version}, tex(didotbo9a.vf) = %{tl_version}
Provides:       tex(didotdenomnums8a.vf) = %{tl_version}
Provides:       tex(didoti8a.vf) = %{tl_version}, tex(didoti9a.vf) = %{tl_version}
Provides:       tex(didotnumnums8a.vf) = %{tl_version}, tex(didoto8a.vf) = %{tl_version}
Provides:       tex(didoto9a.vf) = %{tl_version}, tex(didotrg8a.vf) = %{tl_version}
Provides:       tex(didotrg9a.vf) = %{tl_version}, tex(didotsc8a.vf) = %{tl_version}
Provides:       tex(didotsc9a.vf) = %{tl_version}, tex(didotsco8a.vf) = %{tl_version}
Provides:       tex(didotsco9a.vf) = %{tl_version}, tex(didottabnums8a.vf) = %{tl_version}
Provides:       tex(didotui8a.vf) = %{tl_version}, tex(didotui9a.vf) = %{tl_version}
Provides:       tex(gdidotb6a.vf) = %{tl_version}, tex(gdidotbi6a.vf) = %{tl_version}
Provides:       tex(gdidoti6a.vf) = %{tl_version}, tex(gdidotrg6a.vf) = %{tl_version}
Provides:       tex(gdidotsc6a.vf) = %{tl_version}, tex(gdidotsco6a.vf) = %{tl_version}
Provides:       tex(gfsudidotmath8a.vf) = %{tl_version}, tex(golgai6a.vf) = %{tl_version}
Provides:       tex(golgaui6a.vf) = %{tl_version}, tex(gfsdidot.sty) = %{tl_version}
Provides:       tex(lgrudidot.fd) = %{tl_version}, tex(omludidot.fd) = %{tl_version}
Provides:       tex(ot1udidot.fd) = %{tl_version}, tex(t1udidot.fd) = %{tl_version}
Provides:       tex(uudidotnums.fd) = %{tl_version}

%description -n texlive-gfsdidot
The design of Didot's 1805 Greek typeface was influenced by the
neoclassical ideals of the late 18th century. The font was
brought to Greece at the time of the 1821 Greek Revolution, by
Didot's son, and was very widely used. The present version is
provided by the Greek Font Society. The font supports the Greek
alphabet, and is accompanied by a matching Latin alphabet based
on Zapf's Palatino. LaTeX support is provided, using the OT1,
T1 and LGR encodings.

%package -n texlive-gfsdidot-doc
Summary:        Documentation for gfsdidot
Version:        svn46310
Provides:       tex-gfsdidot-doc
AutoReqProv:    No

%description -n texlive-gfsdidot-doc
Documentation for gfsdidot

%package -n texlive-gfsneohellenic
Provides:       tex-gfsneohellenic = %{tl_version}
License:        LPPL
Summary:        A Greek font in the Neo-Hellenic style
Version:        svn31979.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(neohellenic.enc) = %{tl_version}, tex(neohellenicdenomnums.enc) = %{tl_version}
Provides:       tex(neohellenicec.enc) = %{tl_version}, tex(neohellenicecsc.enc) = %{tl_version}
Provides:       tex(neohellenicel.enc) = %{tl_version}, tex(neohellenicelsc.enc) = %{tl_version}
Provides:       tex(neohellenicmath.enc) = %{tl_version}
Provides:       tex(neohellenicnumnums.enc) = %{tl_version}
Provides:       tex(neohellenicsc.enc) = %{tl_version}, tex(neohellenictabnums.enc) = %{tl_version}
Provides:       tex(gfsneohellenic.map) = %{tl_version}, tex(GFSNeohellenic.otf) = %{tl_version}
Provides:       tex(GFSNeohellenicBold.otf) = %{tl_version}
Provides:       tex(GFSNeohellenicBoldIt.otf) = %{tl_version}
Provides:       tex(GFSNeohellenicIt.otf) = %{tl_version}
Provides:       tex(gfsneohellenicmath8a.tfm) = %{tl_version}
Provides:       tex(gfsneohellenicmath8r.tfm) = %{tl_version}
Provides:       tex(gneohellenicb6a.tfm) = %{tl_version}
Provides:       tex(gneohellenicb6r.tfm) = %{tl_version}
Provides:       tex(gneohellenicbi6a.tfm) = %{tl_version}
Provides:       tex(gneohellenicbi6r.tfm) = %{tl_version}
Provides:       tex(gneohellenicbo6a.tfm) = %{tl_version}
Provides:       tex(gneohellenicbo6r.tfm) = %{tl_version}
Provides:       tex(gneohellenici6a.tfm) = %{tl_version}
Provides:       tex(gneohellenici6r.tfm) = %{tl_version}
Provides:       tex(gneohellenico6a.tfm) = %{tl_version}
Provides:       tex(gneohellenico6r.tfm) = %{tl_version}
Provides:       tex(gneohellenicrg6a.tfm) = %{tl_version}
Provides:       tex(gneohellenicrg6r.tfm) = %{tl_version}
Provides:       tex(gneohellenicsc6a.tfm) = %{tl_version}
Provides:       tex(gneohellenicsc6r.tfm) = %{tl_version}
Provides:       tex(gneohellenicsco6a.tfm) = %{tl_version}
Provides:       tex(gneohellenicsco6r.tfm) = %{tl_version}
Provides:       tex(neohellenicb8a.tfm) = %{tl_version}, tex(neohellenicb8r.tfm) = %{tl_version}
Provides:       tex(neohellenicb9a.tfm) = %{tl_version}, tex(neohellenicb9r.tfm) = %{tl_version}
Provides:       tex(neohellenicbi8a.tfm) = %{tl_version}
Provides:       tex(neohellenicbi8r.tfm) = %{tl_version}
Provides:       tex(neohellenicbi9a.tfm) = %{tl_version}
Provides:       tex(neohellenicbi9r.tfm) = %{tl_version}
Provides:       tex(neohellenicbo8a.tfm) = %{tl_version}
Provides:       tex(neohellenicbo8r.tfm) = %{tl_version}
Provides:       tex(neohellenicbo9a.tfm) = %{tl_version}
Provides:       tex(neohellenicbo9r.tfm) = %{tl_version}
Provides:       tex(neohellenicdenomnums8a.tfm) = %{tl_version}
Provides:       tex(neohellenicdenomnums8r.tfm) = %{tl_version}
Provides:       tex(neohellenici8a.tfm) = %{tl_version}, tex(neohellenici8r.tfm) = %{tl_version}
Provides:       tex(neohellenici9a.tfm) = %{tl_version}, tex(neohellenici9r.tfm) = %{tl_version}
Provides:       tex(neohellenicnumnums8a.tfm) = %{tl_version}
Provides:       tex(neohellenicnumnums8r.tfm) = %{tl_version}
Provides:       tex(neohellenico8a.tfm) = %{tl_version}, tex(neohellenico8r.tfm) = %{tl_version}
Provides:       tex(neohellenico9a.tfm) = %{tl_version}, tex(neohellenico9r.tfm) = %{tl_version}
Provides:       tex(neohellenicrg8a.tfm) = %{tl_version}
Provides:       tex(neohellenicrg8r.tfm) = %{tl_version}
Provides:       tex(neohellenicrg9a.tfm) = %{tl_version}
Provides:       tex(neohellenicrg9r.tfm) = %{tl_version}
Provides:       tex(neohellenicsc8a.tfm) = %{tl_version}
Provides:       tex(neohellenicsc8r.tfm) = %{tl_version}
Provides:       tex(neohellenicsc9a.tfm) = %{tl_version}
Provides:       tex(neohellenicsc9r.tfm) = %{tl_version}
Provides:       tex(neohellenicsco8a.tfm) = %{tl_version}
Provides:       tex(neohellenicsco8r.tfm) = %{tl_version}
Provides:       tex(neohellenicsco9a.tfm) = %{tl_version}
Provides:       tex(neohellenicsco9r.tfm) = %{tl_version}
Provides:       tex(neohellenictabnums8a.tfm) = %{tl_version}
Provides:       tex(neohellenictabnums8r.tfm) = %{tl_version}
Provides:       tex(GFSNeohellenic-Bold.pfb) = %{tl_version}
Provides:       tex(GFSNeohellenic-BoldItalic.pfb) = %{tl_version}
Provides:       tex(GFSNeohellenic-Italic.pfb) = %{tl_version}
Provides:       tex(GFSNeohellenic-Regular.pfb) = %{tl_version}
Provides:       tex(gfsneohellenicmath8a.vf) = %{tl_version}
Provides:       tex(gneohellenicb6a.vf) = %{tl_version}, tex(gneohellenicbi6a.vf) = %{tl_version}
Provides:       tex(gneohellenicbo6a.vf) = %{tl_version}
Provides:       tex(gneohellenici6a.vf) = %{tl_version}, tex(gneohellenico6a.vf) = %{tl_version}
Provides:       tex(gneohellenicrg6a.vf) = %{tl_version}
Provides:       tex(gneohellenicsc6a.vf) = %{tl_version}
Provides:       tex(gneohellenicsco6a.vf) = %{tl_version}
Provides:       tex(neohellenicb8a.vf) = %{tl_version}, tex(neohellenicb9a.vf) = %{tl_version}
Provides:       tex(neohellenicbi8a.vf) = %{tl_version}, tex(neohellenicbi9a.vf) = %{tl_version}
Provides:       tex(neohellenicbo8a.vf) = %{tl_version}, tex(neohellenicbo9a.vf) = %{tl_version}
Provides:       tex(neohellenicdenomnums8a.vf) = %{tl_version}
Provides:       tex(neohellenici8a.vf) = %{tl_version}, tex(neohellenici9a.vf) = %{tl_version}
Provides:       tex(neohellenicnumnums8a.vf) = %{tl_version}
Provides:       tex(neohellenico8a.vf) = %{tl_version}, tex(neohellenico9a.vf) = %{tl_version}
Provides:       tex(neohellenicrg8a.vf) = %{tl_version}, tex(neohellenicrg9a.vf) = %{tl_version}
Provides:       tex(neohellenicsc8a.vf) = %{tl_version}, tex(neohellenicsc9a.vf) = %{tl_version}
Provides:       tex(neohellenicsco8a.vf) = %{tl_version}
Provides:       tex(neohellenicsco9a.vf) = %{tl_version}
Provides:       tex(neohellenictabnums8a.vf) = %{tl_version}
Provides:       tex(gfsneohellenic.sty) = %{tl_version}, tex(lgrneohellenic.fd) = %{tl_version}
Provides:       tex(omlneohellenic.fd) = %{tl_version}, tex(ot1neohellenic.fd) = %{tl_version}
Provides:       tex(t1neohellenic.fd) = %{tl_version}, tex(uneohellenicnums.fd) = %{tl_version}

%description -n texlive-gfsneohellenic
The NeoHellenic style evolved in academic circles in the 19th
and 20th century; the present font follows a cut commissioned
from Monotype in 1927. The present version was provided by the
Greek Font Society. The font supports both Greek and Latin
characters, and has been adjusted to work well with the
cmbright fonts for mathematics support. LaTeX support of the
fonts is provided, offering OT1, T1 and LGR encodings.

%package -n texlive-gfsneohellenic-doc
Summary:        Documentation for gfsneohellenic
Version:        svn31979.0

Provides:       tex-gfsneohellenic-doc
AutoReqProv:    No

%description -n texlive-gfsneohellenic-doc
Documentation for gfsneohellenic

%package -n texlive-gfssolomos
Provides:       tex-gfssolomos = %{tl_version}
License:        OFL
Summary:        A Greek-alphabet font
Version:        svn18651.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(gpsolomos.enc) = %{tl_version}, tex(gfssolomos.map) = %{tl_version}
Provides:       tex(GFSSolomos.otf) = %{tl_version}, tex(gsolomos8a.tfm) = %{tl_version}
Provides:       tex(gsolomos8r.tfm) = %{tl_version}, tex(GFSSolomos-Regular.pfb) = %{tl_version}
Provides:       tex(gsolomos8a.vf) = %{tl_version}, tex(gfssolomos.sty) = %{tl_version}
Provides:       tex(lgrsolomos.fd) = %{tl_version}

%description -n texlive-gfssolomos
Solomos is a font which traces its descent from a
calligraphically-inspired font of the mid-19th century. LaTeX
support, for use with the LGR encoding only, is provided.

%package -n texlive-gfssolomos-doc
Summary:        Documentation for gfssolomos
Version:        svn18651.1.0

Provides:       tex-gfssolomos-doc
AutoReqProv:    No

%description -n texlive-gfssolomos-doc
Documentation for gfssolomos

%package -n texlive-gillcm
Provides:       tex-gillcm = %{tl_version}
License:        BSD
Summary:        Alternative unslanted italic Computer Modern fonts
Version:        svn19878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmg.map) = %{tl_version}, tex(cmgb8r.tfm) = %{tl_version}
Provides:       tex(cmgbi7t.tfm) = %{tl_version}, tex(cmgbi8c.tfm) = %{tl_version}
Provides:       tex(cmgbi8r.tfm) = %{tl_version}, tex(cmgbi8t.tfm) = %{tl_version}
Provides:       tex(cmgbiu7t.tfm) = %{tl_version}, tex(cmgbiu8c.tfm) = %{tl_version}
Provides:       tex(cmgbiu8r.tfm) = %{tl_version}, tex(cmgbiu8t.tfm) = %{tl_version}
Provides:       tex(cmgm8r.tfm) = %{tl_version}, tex(cmgmi7t.tfm) = %{tl_version}
Provides:       tex(cmgmi8c.tfm) = %{tl_version}, tex(cmgmi8r.tfm) = %{tl_version}
Provides:       tex(cmgmi8t.tfm) = %{tl_version}, tex(cmgmiu7t.tfm) = %{tl_version}
Provides:       tex(cmgmiu8c.tfm) = %{tl_version}, tex(cmgmiu8r.tfm) = %{tl_version}
Provides:       tex(cmgmiu8t.tfm) = %{tl_version}, tex(cmgbi7t.vf) = %{tl_version}
Provides:       tex(cmgbi8c.vf) = %{tl_version}, tex(cmgbi8t.vf) = %{tl_version}
Provides:       tex(cmgbiu7t.vf) = %{tl_version}, tex(cmgbiu8c.vf) = %{tl_version}
Provides:       tex(cmgbiu8t.vf) = %{tl_version}, tex(cmgmi7t.vf) = %{tl_version}
Provides:       tex(cmgmi8c.vf) = %{tl_version}, tex(cmgmi8t.vf) = %{tl_version}
Provides:       tex(cmgmiu7t.vf) = %{tl_version}, tex(cmgmiu8c.vf) = %{tl_version}
Provides:       tex(cmgmiu8t.vf) = %{tl_version}, tex(gillcm.sty) = %{tl_version}
Provides:       tex(ot1cmg.fd) = %{tl_version}, tex(t1cmg.fd) = %{tl_version}
Provides:       tex(ts1cmg.fd) = %{tl_version}

%description -n texlive-gillcm
This is a demonstration of the use of virtual fonts for unusual
effects: the package implements an old idea of Eric Gill. The
package was written for the author's talk at TUG 2010.

%package -n texlive-gillcm-doc
Summary:        Documentation for gillcm
Version:        svn19878.1.1

Provides:       tex-gillcm-doc
AutoReqProv:    No

%description -n texlive-gillcm-doc
Documentation for gillcm

%package -n texlive-gillius
Provides:       tex-gillius = %{tl_version}
License:        GPLv2+
Summary:        Gillius fonts with LaTeX support
Version:        svn32068.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(gls_4bsedw.enc) = %{tl_version}, tex(gls_a6mi7n.enc) = %{tl_version}
Provides:       tex(gls_az7pev.enc) = %{tl_version}, tex(gls_bg5e7z.enc) = %{tl_version}
Provides:       tex(gls_efuo7w.enc) = %{tl_version}, tex(gls_lf6eoq.enc) = %{tl_version}
Provides:       tex(gls_pqq4vh.enc) = %{tl_version}, tex(gls_shb4ap.enc) = %{tl_version}
Provides:       tex(gillius.map) = %{tl_version}, tex(GilliusADF-Bold.otf) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic.otf) = %{tl_version}
Provides:       tex(GilliusADF-Italic.otf) = %{tl_version}
Provides:       tex(GilliusADF-Regular.otf) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold.otf) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic.otf) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic.otf) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular.otf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold.otf) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic.otf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic.otf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular.otf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold.otf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic.otf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic.otf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular.otf) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ot1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(GilliusADF-Bold.pfb) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic.pfb) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADF-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADF-Italic.pfb) = %{tl_version}
Provides:       tex(GilliusADF-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADF-Regular.pfb) = %{tl_version}
Provides:       tex(GilliusADF-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold.pfb) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic.pfb) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic.pfb) = %{tl_version}
Provides:       tex(GilliusADFCond-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular.pfb) = %{tl_version}
Provides:       tex(GilliusADFCond-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular.pfb) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADF-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADF-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFCond-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ot1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(GilliusADFNo2Cond-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(LY1GilliusADF-LF.fd) = %{tl_version}
Provides:       tex(LY1GilliusADFCond-LF.fd) = %{tl_version}
Provides:       tex(LY1GilliusADFNoTwo-LF.fd) = %{tl_version}
Provides:       tex(LY1GilliusADFNoTwoCond-LF.fd) = %{tl_version}
Provides:       tex(OT1GilliusADF-LF.fd) = %{tl_version}
Provides:       tex(OT1GilliusADFCond-LF.fd) = %{tl_version}
Provides:       tex(OT1GilliusADFNoTwo-LF.fd) = %{tl_version}
Provides:       tex(OT1GilliusADFNoTwoCond-LF.fd) = %{tl_version}
Provides:       tex(T1GilliusADF-LF.fd) = %{tl_version}, tex(T1GilliusADFCond-LF.fd) = %{tl_version}
Provides:       tex(T1GilliusADFNoTwo-LF.fd) = %{tl_version}
Provides:       tex(T1GilliusADFNoTwoCond-LF.fd) = %{tl_version}
Provides:       tex(TS1GilliusADF-LF.fd) = %{tl_version}
Provides:       tex(TS1GilliusADFCond-LF.fd) = %{tl_version}
Provides:       tex(TS1GilliusADFNoTwo-LF.fd) = %{tl_version}
Provides:       tex(TS1GilliusADFNoTwoCond-LF.fd) = %{tl_version}
Provides:       tex(gillius.sty) = %{tl_version}, tex(gillius2.sty) = %{tl_version}

%description -n texlive-gillius
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Gillius and Gillius No. 2 families of sans
serif fonts and condensed versions of them, designed by Hirwen
Harendal. According to the designer, the fonts were inspired by
Gill Sans.

%package -n texlive-gillius-doc
Summary:        Documentation for gillius
Version:        svn32068.0

Provides:       tex-gillius-doc
AutoReqProv:    No

%description -n texlive-gillius-doc
Documentation for gillius

%package -n texlive-gnu-freefont
Provides:       tex-gnu-freefont = %{tl_version}
License:        GPLv3+
Summary:        A Unicode font, with rather wide coverage
Version:        svn29349.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(FreeMono.otf) = %{tl_version}, tex(FreeMonoBold.otf) = %{tl_version}
Provides:       tex(FreeMonoBoldOblique.otf) = %{tl_version}
Provides:       tex(FreeMonoOblique.otf) = %{tl_version}
Provides:       tex(FreeSans.otf) = %{tl_version}, tex(FreeSansBold.otf) = %{tl_version}
Provides:       tex(FreeSansBoldOblique.otf) = %{tl_version}
Provides:       tex(FreeSansOblique.otf) = %{tl_version}
Provides:       tex(FreeSerif.otf) = %{tl_version}, tex(FreeSerifBold.otf) = %{tl_version}
Provides:       tex(FreeSerifBoldItalic.otf) = %{tl_version}
Provides:       tex(FreeSerifItalic.otf) = %{tl_version}
Provides:       tex(FreeMono.ttf) = %{tl_version}, tex(FreeMonoBold.ttf) = %{tl_version}
Provides:       tex(FreeMonoBoldOblique.ttf) = %{tl_version}
Provides:       tex(FreeMonoOblique.ttf) = %{tl_version}
Provides:       tex(FreeSans.ttf) = %{tl_version}, tex(FreeSansBold.ttf) = %{tl_version}
Provides:       tex(FreeSansBoldOblique.ttf) = %{tl_version}
Provides:       tex(FreeSansOblique.ttf) = %{tl_version}
Provides:       tex(FreeSerif.ttf) = %{tl_version}, tex(FreeSerifBold.ttf) = %{tl_version}
Provides:       tex(FreeSerifBoldItalic.ttf) = %{tl_version}
Provides:       tex(FreeSerifItalic.ttf) = %{tl_version}

%description -n texlive-gnu-freefont
The package provides a set of outline (i.e. OpenType) fonts
covering as much as possible of the Unicode character set. The
set consists of three typefaces: one monospaced and two
proportional (one with uniform and one with modulated stroke).

%package -n texlive-gnu-freefont-doc
Summary:        Documentation for gnu-freefont
Version:        svn29349.0

Provides:       tex-gnu-freefont-doc
AutoReqProv:    No

%description -n texlive-gnu-freefont-doc
Documentation for gnu-freefont

%package -n texlive-gothic
Provides:       tex-gothic = %{tl_version}
License:        Public Domain
Summary:        A collection of old German-style fonts
Version:        svn38263.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cmfrak.tfm) = %{tl_version}, tex(schwell.tfm) = %{tl_version}
Provides:       tex(suet14.tfm) = %{tl_version}, tex(yfrak.tfm) = %{tl_version}
Provides:       tex(ygoth.tfm) = %{tl_version}, tex(yinit.tfm) = %{tl_version}
Provides:       tex(ysmfrak.tfm) = %{tl_version}, tex(yswab.tfm) = %{tl_version}

%description -n texlive-gothic
A collection of fonts that reproduce those used in "old German"
printing and handwriting. The set comprises Gothic, Schwabacher
and Fraktur fonts, a pair of handwriting fonts, Sutterlin and
Schwell, and a font containing decorative initials. In
addition, there are two re-encoding packages for Haralambous's
fonts, providing T1, using virtual fonts, and OT1 and T1, using
Metafont.

%package -n texlive-gothic-doc
Summary:        Documentation for gothic
Version:        svn38263.0

Provides:       tex-gothic-doc
AutoReqProv:    No

%description -n texlive-gothic-doc
Documentation for gothic

%package -n texlive-greenpoint
Provides:       tex-greenpoint = %{tl_version}
License:        GPL+
Summary:        The Green Point logo
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(greenpoint.tfm) = %{tl_version}

%description -n texlive-greenpoint
A Metafont-implementation of the logo commonly known as 'Der
Grune Punkt' ('The Green Point'). In Austria, it can be found
on nearly every bottle. It should not be confused with the
'Recycle'-logo, implemented by Ian Green.

%package -n texlive-greenpoint-doc
Summary:        Documentation for greenpoint
Version:        svn15878.0

Provides:       tex-greenpoint-doc
AutoReqProv:    No

%description -n texlive-greenpoint-doc
Documentation for greenpoint

%package -n texlive-grotesq
Provides:       tex-grotesq = %{tl_version}
License:        GPL+
Summary:        URW Grotesq font pack for LaTeX
Version:        svn35859.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(ugq.map) = %{tl_version}, tex(ugqb7t.tfm) = %{tl_version}
Provides:       tex(ugqb8a.tfm) = %{tl_version}, tex(ugqb8c.tfm) = %{tl_version}
Provides:       tex(ugqb8r.tfm) = %{tl_version}, tex(ugqb8t.tfm) = %{tl_version}
Provides:       tex(ugqbo7t.tfm) = %{tl_version}, tex(ugqbo8c.tfm) = %{tl_version}
Provides:       tex(ugqbo8r.tfm) = %{tl_version}, tex(ugqbo8t.tfm) = %{tl_version}
Provides:       tex(ugqb8a.pfb) = %{tl_version}, tex(ugqb7t.vf) = %{tl_version}
Provides:       tex(ugqb8c.vf) = %{tl_version}, tex(ugqb8t.vf) = %{tl_version}
Provides:       tex(ugqbo7t.vf) = %{tl_version}, tex(ugqbo8c.vf) = %{tl_version}
Provides:       tex(ugqbo8t.vf) = %{tl_version}, tex(ot1ugq.fd) = %{tl_version}
Provides:       tex(t1ugq.fd) = %{tl_version}, tex(ts1ugq.fd) = %{tl_version}

%description -n texlive-grotesq
The directory contains a copy of the Type 1 font "URW Grotesq
2031 Bold' released under the GPL by URW, with supporting files
for use with (La)TeX.

%package -n texlive-grotesq-doc
Summary:        Documentation for grotesq
Version:        svn35859.0

Provides:       tex-grotesq-doc
AutoReqProv:    No

%description -n texlive-grotesq-doc
Documentation for grotesq


%package -n texlive-gamebook
Provides:       tex-gamebook = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset gamebooks and other interactive novels
Version:        svn24714.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(fancyhdr.sty), tex(extramarks.sty), tex(titlesec.sty)
Requires:       tex(enumitem.sty), tex(draftwatermark.sty)
Requires:       tex(scrtime.sty), tex(prelim2e.sty)
Provides:       tex(gamebook.sty) = %{tl_version}

%description -n texlive-gamebook
This package provides the means in order to lay-out gamebooks
with LaTeX. A simple gamebook example is included with the
package, and acts as a tutorial.

%package -n texlive-gamebook-doc
Summary:        Documentation for gamebook
Version:        svn24714.1.0

Provides:       tex-gamebook-doc
AutoReqProv:    No

%description -n texlive-gamebook-doc
Documentation for gamebook

%package -n texlive-go
Provides:       tex-go = %{tl_version}
License:        Public Domain
Summary:        Fonts and macros for typesetting go games
Version:        svn28628.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(go10.tfm) = %{tl_version}, tex(go15.tfm) = %{tl_version}
Provides:       tex(go1bla10.tfm) = %{tl_version}, tex(go1bla15.tfm) = %{tl_version}
Provides:       tex(go1bla20.tfm) = %{tl_version}, tex(go1whi10.tfm) = %{tl_version}
Provides:       tex(go1whi15.tfm) = %{tl_version}, tex(go1whi20.tfm) = %{tl_version}
Provides:       tex(go20.tfm) = %{tl_version}, tex(go2bla10.tfm) = %{tl_version}
Provides:       tex(go2bla15.tfm) = %{tl_version}, tex(go2bla20.tfm) = %{tl_version}
Provides:       tex(go2whi10.tfm) = %{tl_version}, tex(go2whi15.tfm) = %{tl_version}
Provides:       tex(go2whi20.tfm) = %{tl_version}, tex(gosign50.tfm) = %{tl_version}
Provides:       tex(go.sty) = %{tl_version}

%description -n texlive-go
The macros provide for nothing more complicated than the
standard 19x19 board; the fonts are written in Metafont.

%package -n texlive-go-doc
Summary:        Documentation for go
Version:        svn28628.0

Provides:       tex-go-doc
AutoReqProv:    No

%description -n texlive-go-doc
Documentation for go

%package -n texlive-gates
Provides:       tex-gates = %{tl_version}
License:        LPPL
Summary:        Support for writing modular and customisable code
Version:        svn29803.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gates.sty) = %{tl_version}, tex(gates.tex) = %{tl_version}
Provides:       tex(t-gates.tex) = %{tl_version}

%description -n texlive-gates
The package provides the means of writing code in a modular
fashion: big macros or functions are divided into small chunks
(called gates) with names, which can be externally controlled
(e.g. they can be disabled, subjected to conditionals,
loops...) and/or augmented with new chunks. Thus complex code
may easily be customised without having to rewrite it, or even
understand its implementation: the behavior of existing gates
can be modified, and new ones can be added, without endangering
the whole design. This allows code to be hacked in ways the
original authors might have never envisioned. The gates package
is implemented independently for both TeX and Lua. The TeX
implementation, running in any current environment, requires
the texapi package, whereas the Lua version can be run with any
Lua interpreter, not just LuaTeX.

%package -n texlive-gates-doc
Summary:        Documentation for gates
Version:        svn29803.0.2

Provides:       tex-gates-doc
AutoReqProv:    No

%description -n texlive-gates-doc
Documentation for gates

%package -n texlive-genmisc
Provides:       tex-genmisc = %{tl_version}
License:        LPPL
Summary:        genmisc package
Version:        svn45851
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(anti.tex) = %{tl_version}, tex(apldef.tex) = %{tl_version}
Provides:       tex(arabic.tex) = %{tl_version}, tex(backgrnd.tex) = %{tl_version}
Provides:       tex(balancedquotes.sty) = %{tl_version}, tex(chessmin.tex) = %{tl_version}
Provides:       tex(compare.tex) = %{tl_version}, tex(cropmark.sty) = %{tl_version}
Provides:       tex(cropmark.tex) = %{tl_version}, tex(croptest.tex) = %{tl_version}
Provides:       tex(dayofweek.tex) = %{tl_version}, tex(daytime.sty) = %{tl_version}
Provides:       tex(default.sty) = %{tl_version}, tex(dow.tex) = %{tl_version}
Provides:       tex(emtrees.tex) = %{tl_version}, tex(endnote.tex) = %{tl_version}
Provides:       tex(fakebold.tex) = %{tl_version}, tex(hep.tex) = %{tl_version}
Provides:       tex(inscrutable.tex) = %{tl_version}, tex(laps.tex) = %{tl_version}
Provides:       tex(letterspacing.tex) = %{tl_version}, tex(longdiv.tex) = %{tl_version}
Provides:       tex(mandel.tex) = %{tl_version}, tex(mathlig.tex) = %{tl_version}
Provides:       tex(nth.sty) = %{tl_version}, tex(outerhbox.sty) = %{tl_version}
Provides:       tex(pagereference.tex) = %{tl_version}, tex(quotation.tex) = %{tl_version}
Provides:       tex(ragged.sty) = %{tl_version}, tex(random.tex) = %{tl_version}
Provides:       tex(ruler.tex) = %{tl_version}, tex(selectpage.tex) = %{tl_version}
Provides:       tex(shadebox.tex) = %{tl_version}, tex(swrule.sty) = %{tl_version}
Provides:       tex(underlin.tex) = %{tl_version}, tex(undertilde.tex) = %{tl_version}
Provides:       tex(verbatim.tex) = %{tl_version}, tex(weekday.sty) = %{tl_version}
Provides:       tex(wiggly.tex) = %{tl_version}, tex(zip.tex) = %{tl_version}

%description -n texlive-genmisc
genmisc package

%package -n texlive-gb4e
Provides:       tex-gb4e = %{tl_version}
License:        LPPL 1.2
Summary:        Linguistic tools
Version:        svn19216.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cgloss4e.sty) = %{tl_version}, tex(gb4e.sty) = %{tl_version}

%description -n texlive-gb4e
Provides an environment for linguistic examples, tools for
glosses, and various other goodies. The code was developed from
the midnight and covington packages.

%package -n texlive-gb4e-doc
Summary:        Documentation for gb4e
Version:        svn19216.0

Provides:       tex-gb4e-doc
AutoReqProv:    No

%description -n texlive-gb4e-doc
Documentation for gb4e

%package -n texlive-gmverse
Provides:       tex-gmverse = %{tl_version}
License:        LPPL
Summary:        A package for typesetting (short) poems
Version:        svn29803.v0.73

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gmverse.sty) = %{tl_version}

%description -n texlive-gmverse
A redefinition of the verse environment to make the \\ command
optional for line ends and to give it a possibility of optical
centering and `right-hanging' alignment of lines broken because
of length.

%package -n texlive-gmverse-doc
Summary:        Documentation for gmverse
Version:        svn29803.v0.73

Provides:       tex-gmverse-doc
AutoReqProv:    No

%description -n texlive-gmverse-doc
Documentation for gmverse

%package -n texlive-ghab
Provides:       tex-ghab = %{tl_version}
License:        LPPL
Summary:        Typeset ghab boxes in LaTeX
Version:        svn29803.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(biditools.sty)
Provides:       tex(ghab.sty) = %{tl_version}

%description -n texlive-ghab
The package defines a command \darghab that will typeset its
argument in a box with a decorated frame. The width of the box
may be set using an optional argument.

%package -n texlive-ghab-doc
Summary:        Documentation for ghab
Version:        svn29803.0.5

Provides:       tex-ghab-doc
AutoReqProv:    No

%description -n texlive-ghab-doc
Documentation for ghab

%package -n texlive-gost
Provides:       tex-gost = %{tl_version}
License:        LPPL
Summary:        BibTeX styles to format according to GOST
Version:        svn44131
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-gost
BibTeX styles to format bibliographies in English, Russian or
Ukrainian according to GOST 7.0.5-2008 or GOST 7.1-2003. Both 8-
bit and Unicode (UTF-8) versions of each BibTeX style, in each
case offering a choice of sorted and unsorted. Further, a set
of three styles (which do not conform to current standards) are
retained for backwards compatibility.

%package -n texlive-gost-doc
Summary:        Documentation for gost
Version:        svn44131
Provides:       tex-gost-doc
AutoReqProv:    No

%description -n texlive-gost-doc
Documentation for gost

%package -n texlive-gentle-doc
Summary:        Documentation for gentle
Version:        svn15878.0

Provides:       tex-gentle-doc
AutoReqProv:    No

%description -n texlive-gentle-doc
Documentation for gentle

%package -n texlive-guide-to-latex-doc
Summary:        Documentation for guide-to-latex
Version:        svn15878.0

Provides:       tex-guide-to-latex-doc
AutoReqProv:    No

%description -n texlive-guide-to-latex-doc
Documentation for guide-to-latex

%package -n texlive-geometry-de-doc
Summary:        Documentation for geometry-de
Version:        svn21882.1.1

Provides:       tex-geometry-de-doc
AutoReqProv:    No

%description -n texlive-geometry-de-doc
Documentation for geometry-de

%package -n texlive-german
Provides:       tex-german = %{tl_version}
License:        LPPL
Summary:        Support for German typography
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(german.sty) = %{tl_version}, tex(ngerman.sty) = %{tl_version}

%description -n texlive-german
Supports the new German orthography (neue deutsche
Rechtschreibung).

%package -n texlive-german-doc
Summary:        Documentation for german
Version:        svn42428
Provides:       tex-german-doc
AutoReqProv:    No

%description -n texlive-german-doc
Documentation for german

%package -n texlive-germbib
Provides:       tex-germbib = %{tl_version}
License:        Bibtex
Summary:        German variants of standard BibTeX styles
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(german.sty)
Provides:       tex(bibgerm.sty) = %{tl_version}, tex(mynormal.sty) = %{tl_version}

%description -n texlive-germbib
A development of the (old) german.sty, this bundle provides
German packages, BibTeX styles and documentary examples, for
writing documents with bibliographies. The author has since
developed the babelbib bundle, which (he asserts) supersedes
germbib.

%package -n texlive-germbib-doc
Summary:        Documentation for germbib
Version:        svn15878.0

Provides:       tex-germbib-doc
AutoReqProv:    No

%description -n texlive-germbib-doc
Documentation for germbib

%package -n texlive-germkorr
Provides:       tex-germkorr = %{tl_version}
License:        GPL+
Summary:        Change kerning for german quotation marks
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(germkorr.sty) = %{tl_version}

%description -n texlive-germkorr
The package germcorr has to be loaded after the package german.
It brings some letters like T nearer to german single and
double quotes even when that letter wears a standard accent
like "`\.T"'.

%package -n texlive-germkorr-doc
Summary:        Documentation for germkorr
Version:        svn15878.1.0

Provides:       tex-germkorr-doc
AutoReqProv:    No

%description -n texlive-germkorr-doc
Documentation for germkorr

%package -n texlive-gfsbaskerville
Provides:       tex-gfsbaskerville = %{tl_version}
License:        LPPL
Summary:        A Greek font, from one such by Baskerville
Version:        svn19440.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(gpgfsbaskerville.enc) = %{tl_version}
Provides:       tex(gfsbaskerville.map) = %{tl_version}, tex(GFSBaskerville.otf) = %{tl_version}
Provides:       tex(ggfsbaskervillerg6a.tfm) = %{tl_version}
Provides:       tex(ggfsbaskervillerg6r.tfm) = %{tl_version}
Provides:       tex(GFSBaskerville-Regular.pfb) = %{tl_version}
Provides:       tex(ggfsbaskervillerg6a.vf) = %{tl_version}
Provides:       tex(gfsbaskerville.sty) = %{tl_version}, tex(lgrgfsbaskerville.fd) = %{tl_version}

%description -n texlive-gfsbaskerville
The font is a digital implementation of Baskerville's classic
Greek font, provided by the Greek Font Society. The font covers
Greek only, and LaTeX support provides for the use of LGR
encoding.

%package -n texlive-gfsbaskerville-doc
Summary:        Documentation for gfsbaskerville
Version:        svn19440.1.0

Provides:       tex-gfsbaskerville-doc
AutoReqProv:    No

%description -n texlive-gfsbaskerville-doc
Documentation for gfsbaskerville

%package -n texlive-gfsporson
Provides:       tex-gfsporson = %{tl_version}
License:        LPPL
Summary:        A Greek font, originally from Porson
Version:        svn18651.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(porsonel.enc) = %{tl_version}, tex(gfsporson.map) = %{tl_version}
Provides:       tex(GFSPorson.otf) = %{tl_version}, tex(gporsonrg6a.tfm) = %{tl_version}
Provides:       tex(gporsonrg6r.tfm) = %{tl_version}, tex(GFSPorson-Regular.pfb) = %{tl_version}
Provides:       tex(gporsonrg6a.vf) = %{tl_version}, tex(gfsporson.sty) = %{tl_version}
Provides:       tex(lgrporson.fd) = %{tl_version}

%description -n texlive-gfsporson
Porson is an elegant Greek font, originally cut at the turn of
the 19th Century in England. The present version has been
provided by the Greek Font Society. The font supports the Greek
alphabet only. LaTeX support is provided, using the LGR
encoding.

%package -n texlive-gfsporson-doc
Summary:        Documentation for gfsporson
Version:        svn18651.1.01

Provides:       tex-gfsporson-doc
AutoReqProv:    No

%description -n texlive-gfsporson-doc
Documentation for gfsporson

%package -n texlive-greek-fontenc
Provides:       tex-greek-fontenc = %{tl_version}
License:        LPPL 1.3
Summary:        LICR macros and encoding definition files for Greek
Version:        svn39606

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(alphabeta-euenc.def) = %{tl_version}
Provides:       tex(alphabeta-lgr.def) = %{tl_version}, tex(alphabeta.sty) = %{tl_version}
Provides:       tex(greek-euenc.def) = %{tl_version}, tex(greek-fontenc.def) = %{tl_version}
Provides:       tex(lgrenc.def) = %{tl_version}, tex(textalpha.sty) = %{tl_version}

%description -n texlive-greek-fontenc
The package provides Greek LICR macro definitions and encoding
definition files for Greek text font encodings for use with
fontenc.

%package -n texlive-greek-fontenc-doc
Summary:        Documentation for greek-fontenc
Version:        svn39606

Provides:       tex-greek-fontenc-doc
AutoReqProv:    No

%description -n texlive-greek-fontenc-doc
Documentation for greek-fontenc

%package -n texlive-greek-inputenc
Provides:       tex-greek-inputenc = %{tl_version}
License:        LPPL 1.3
Summary:        Greek encoding support for inputenc
Version:        svn40613

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(iso-8859-7.def) = %{tl_version}, tex(macgreek.def) = %{tl_version}

%description -n texlive-greek-inputenc
The bundle provides UTF-8, Macintosh Greek encoding and ISO
8859-7 definition files for use with inputenc.

%package -n texlive-greek-inputenc-doc
Summary:        Documentation for greek-inputenc
Version:        svn40613

Provides:       tex-greek-inputenc-doc
AutoReqProv:    No

%description -n texlive-greek-inputenc-doc
Documentation for greek-inputenc

%package -n texlive-greekdates
Provides:       tex-greekdates = %{tl_version}
License:        LPPL
Summary:        Provides ancient Greek day and month names, dates, etc
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty)
Provides:       tex(greekdates.sty) = %{tl_version}

%description -n texlive-greekdates
The package provides easy access to ancient Greek names of days
and months of various regions of Greece. In case the historical
information about a region is not complete, we use the Athenian
name of the month. Moreover commands and options are provided,
in order to completely switch to the "ancient way", commands
such as \today.

%package -n texlive-greekdates-doc
Summary:        Documentation for greekdates
Version:        svn15878.1.0

Provides:       tex-greekdates-doc
AutoReqProv:    No

%description -n texlive-greekdates-doc
Documentation for greekdates

%package -n texlive-greektex
Provides:       tex-greektex = %{tl_version}
License:        Public Domain
Summary:        Fonts for typesetting Greek/English documents
Version:        svn28327.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(greektex.sty) = %{tl_version}

%description -n texlive-greektex
The fonts are based on Silvio Levy's classical Greek fonts;
macros and Greek hyphenation patterns for the fonts' encoding
are also provided.

%package -n texlive-greektex-doc
Summary:        Documentation for greektex
Version:        svn28327.0

Provides:       tex-greektex-doc
AutoReqProv:    No

%description -n texlive-greektex-doc
Documentation for greektex

%package -n texlive-gustlib
Provides:       tex-gustlib = %{tl_version}
License:        LPPL
Summary:        gustlib package
Version:        svn45712
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(biblotex.tex) = %{tl_version}, tex(infr-ex.tex) = %{tl_version}
Provides:       tex(infram.tex) = %{tl_version}, tex(map.tex) = %{tl_version}
Provides:       tex(split.tex) = %{tl_version}, tex(tsp.tex) = %{tl_version}
Provides:       tex(tun.tex) = %{tl_version}, tex(mcol-ex.tex) = %{tl_version}
Provides:       tex(meashor.tex) = %{tl_version}, tex(mimulcol.tex) = %{tl_version}
Provides:       tex(plidxmac.tex) = %{tl_version}, tex(przyklad.tex) = %{tl_version}
Provides:       tex(rbox-ex.tex) = %{tl_version}, tex(roundbox.tex) = %{tl_version}
Provides:       tex(tp-crf.tex) = %{tl_version}, tex(verbatim-dek.tex) = %{tl_version}

%description -n texlive-gustlib
gustlib package

%package -n texlive-gustlib-doc
Summary:        Documentation for gustlib
Version:        svn45712
Provides:       tex-gustlib-doc
AutoReqProv:    No

%description -n texlive-gustlib-doc
Documentation for gustlib

%package -n texlive-gustprog-doc
Summary:        Documentation for gustprog
Version:        svn45712
Provides:       tex-gustprog-doc
AutoReqProv:    No

%description -n texlive-gustprog-doc
Documentation for gustprog

%package -n texlive-genealogytree
Provides:       tex-genealogytree = %{tl_version}
License:        LPPL 1.3
Summary:        Pedigree and genealogical tree diagrams
Version:        svn47539
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tcolorbox.sty)
Provides:       tex(genealogytree.sty) = %{tl_version}, tex(gtrcore.contour.code.tex) = %{tl_version}
Provides:       tex(gtrcore.drawing.code.tex) = %{tl_version}
Provides:       tex(gtrcore.node.code.tex) = %{tl_version}
Provides:       tex(gtrcore.options.code.tex) = %{tl_version}
Provides:       tex(gtrcore.parser.code.tex) = %{tl_version}
Provides:       tex(gtrcore.processing.code.tex) = %{tl_version}
Provides:       tex(gtrcore.symbols.code.tex) = %{tl_version}
Provides:       tex(gtrlang.english.code.tex) = %{tl_version}
Provides:       tex(gtrlang.german.code.tex) = %{tl_version}
Provides:       tex(gtrlib.debug.code.tex) = %{tl_version}
Provides:       tex(gtrlib.templates.code.tex) = %{tl_version}

%description -n texlive-genealogytree
Pedigree and genealogical tree diagrams are proven tools to
visualize genetic and relational connections between
individuals. The naming ("tree") derives from historical family
diagrams. However, even the smallest family entity consisting
of two parents and several children is hardly a 'mathematical'
tree -- it is a more general graph. The package provides a set
of tools to typeset genealogical trees (i.e., to typeset a set
of special graphs for the description of family-like
structures). The package uses an autolayout algorithm which can
be customized, e.g., to prioritize certain paths.

%package -n texlive-genealogytree-doc
Summary:        Documentation for genealogytree
Version:        svn47539
Provides:       tex-genealogytree-doc
AutoReqProv:    No

%description -n texlive-genealogytree-doc
Documentation for genealogytree

%package -n texlive-gincltex
Provides:       tex-gincltex = %{tl_version}
License:        LPPL 1.3
Summary:        Include TeX files as graphics (.tex support for \includegraphics)
Version:        svn23835.0.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(svn-prov.sty), tex(adjustbox.sty)
Provides:       tex(gincltex.sty) = %{tl_version}

%description -n texlive-gincltex
The package builds on the standard LaTeX packages graphics
and/or graphicx and allows external LaTeX source files to be
included, in the same way as graphic files, by
\includegraphics. In effect, then package adds support for the
.tex extension. Some of the lower level operations like
clipping and trimming are implemented using the adjustbox
package which includes native pdflatex support and uses the pgf
pacakge for other output formats.

%package -n texlive-gincltex-doc
Summary:        Documentation for gincltex
Version:        svn23835.0.3

Provides:       tex-gincltex-doc
AutoReqProv:    No

%description -n texlive-gincltex-doc
Documentation for gincltex

%package -n texlive-gnuplottex
Provides:       tex-gnuplottex = %{tl_version}
License:        GPLv2+
Summary:        Embed Gnuplot commands in LaTeX documents
Version:        svn41904
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(latexsym.sty), tex(graphicx.sty), tex(moreverb.sty), tex(keyval.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(gnuplottex.sty) = %{tl_version}

%description -n texlive-gnuplottex
The package extracts Gnuplot code from the document and writes
it to .gnuplot files. If shell escape is enabled, the graph
files are automatically processed and converted to PostScript
or PDF files, which will then be included. If shell escape is
disabled, the user has to run the files through gnuplot, and re-
run the LaTeX job.

%package -n texlive-gnuplottex-doc
Summary:        Documentation for gnuplottex
Version:        svn41904
Provides:       tex-gnuplottex-doc
AutoReqProv:    No

%description -n texlive-gnuplottex-doc
Documentation for gnuplottex

%package -n texlive-gradientframe
Provides:       tex-gradientframe = %{tl_version}
License:        LPPL 1.3
Summary:        Simple gradient frames around objects
Version:        svn21387.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(keyval.sty)
Provides:       tex(gradientframe.sty) = %{tl_version}

%description -n texlive-gradientframe
The package provides a means of drawing graded frames around
objects. The gradients of the frames are drawn using the color
package.

%package -n texlive-gradientframe-doc
Summary:        Documentation for gradientframe
Version:        svn21387.0.2

Provides:       tex-gradientframe-doc
AutoReqProv:    No

%description -n texlive-gradientframe-doc
Documentation for gradientframe

%package -n texlive-grafcet
Provides:       tex-grafcet = %{tl_version}
License:        LPPL
Summary:        Draw Grafcet/SFC with TikZ
Version:        svn22509.1.3.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty), tex(ifsym.sty)
Provides:       tex(grafcet.sty) = %{tl_version}

%description -n texlive-grafcet
The package provides a library (GRAFCET) that can draw Grafcet
Sequential Function Chart (SFC) diagrams, in accordance with EN
60848, using Pgf/TikZ. L'objectif de la librairie GRAFCET est
de permettre le trace de grafcet selon la norme EN 60848 a
partir de Pgf/TikZ.

%package -n texlive-grafcet-doc
Summary:        Documentation for grafcet
Version:        svn22509.1.3.5

Provides:       tex-grafcet-doc
AutoReqProv:    No

%description -n texlive-grafcet-doc
Documentation for grafcet

%package -n texlive-graphviz
Provides:       tex-graphviz = %{tl_version}
License:        LPPL 1.3
Summary:        Write graphviz (dot+neato) inline in LaTeX documents
Version:        svn31517.0.94

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(psfrag.sty)
Provides:       tex(graphviz.sty) = %{tl_version}

%description -n texlive-graphviz
The package allows inline use of graphviz code, in a LaTeX
document.

%package -n texlive-graphviz-doc
Summary:        Documentation for graphviz
Version:        svn31517.0.94

Provides:       tex-graphviz-doc
AutoReqProv:    No

%description -n texlive-graphviz-doc
Documentation for graphviz

%package -n texlive-g-brief
Provides:       tex-g-brief = %{tl_version}
License:        LPPL
Summary:        Letter document class
Version:        svn21140.4.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(babel.sty), tex(inputenc.sty), tex(marvosym.sty), tex(eurosym.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(g-brief.cls) = %{tl_version}, tex(g-brief.sty) = %{tl_version}
Provides:       tex(g-brief2.cls) = %{tl_version}, tex(g-brief2.sty) = %{tl_version}

%description -n texlive-g-brief
Designed for formatting formless letters in German; can also be
used for English (by those who can read the documentation).
There are LaTeX 2.09 documentstyle and LaTeX 2e class files for
both an 'old' and a 'new' version of g-brief.

%package -n texlive-g-brief-doc
Summary:        Documentation for g-brief
Version:        svn21140.4.0.2

Provides:       tex-g-brief-doc
AutoReqProv:    No

%description -n texlive-g-brief-doc
Documentation for g-brief

%package -n texlive-gauss
Provides:       tex-gauss = %{tl_version}
License:        LPPL
Summary:        A package for Gaussian operations
Version:        svn32934.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty)
Provides:       tex(gauss.sty) = %{tl_version}

%description -n texlive-gauss
The gauss package provides configurable tools for producing row
and column operations on matrices (a.k.a. Gaussian operations).

%package -n texlive-gauss-doc
Summary:        Documentation for gauss
Version:        svn32934.0

Provides:       tex-gauss-doc
AutoReqProv:    No

%description -n texlive-gauss-doc
Documentation for gauss

%package -n texlive-gcard
Provides:       tex-gcard = %{tl_version}
License:        LPPL
Summary:        Arrange text on a sheet to fold into a greeting card
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(textpos.sty), tex(graphicx.sty), tex(calc.sty)
Provides:       tex(gcard.sty) = %{tl_version}

%description -n texlive-gcard
The package provides a simple means of producing greeting
cards. It arranges four panels onto a single sheet so that when
the sheet is folded twice the four panels are arranged as front
cover, inside left and right pages, and back cover. It uses the
textpos package for placement on the sheet and the graphicx
package for the necessary rotation. The four panels are set in
minipages for formatting by the user.

%package -n texlive-gcard-doc
Summary:        Documentation for gcard
Version:        svn15878.0

Provides:       tex-gcard-doc
AutoReqProv:    No

%description -n texlive-gcard-doc
Documentation for gcard

%package -n texlive-gcite
Provides:       tex-gcite = %{tl_version}
License:        LPPL 1.3
Summary:        Citations in a reader-friendly style
Version:        svn15878.1.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(biblatex.sty)
Provides:       tex(gcite.sty) = %{tl_version}

%description -n texlive-gcite
The package allows citations in the German style, which is
considered by many to be particularly reader-friendly. The
citation provides a small amount of bibliographic information
in a footnote on the page where each citation is made. It
combines a desire to eliminate unnecessary page-turning with
the look-up efficiency afforded by numeric citations. The
package makes use of BibLaTeX, and is considered experimental;
comment is invited.

%package -n texlive-gcite-doc
Summary:        Documentation for gcite
Version:        svn15878.1.0.1

Provides:       tex-gcite-doc
AutoReqProv:    No

%description -n texlive-gcite-doc
Documentation for gcite

%package -n texlive-gender
Provides:       tex-gender = %{tl_version}
License:        LPPL 1.3
Summary:        Gender neutrality for languages with grammatical gender
Version:        svn36464.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty)
Provides:       tex(gender.sty) = %{tl_version}

%description -n texlive-gender
Many languages -- like German or French -- use masculine and
feminine grammatical genders. There are many ideas how to
promote gender neutrality in those languages. The gender
package uses alternately masculine and feminine forms. It is
also possible to use just one form out of a template.

%package -n texlive-gender-doc
Summary:        Documentation for gender
Version:        svn36464.1.0

Provides:       tex-gender-doc
AutoReqProv:    No

%description -n texlive-gender-doc
Documentation for gender

%package -n texlive-genmpage
Provides:       tex-genmpage = %{tl_version}
License:        LPPL
Summary:        Generalization of LaTeX's minipages
Version:        svn15878.0.3.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(genmpage.sty) = %{tl_version}

%description -n texlive-genmpage
The GenMPage package generalizes LaTeX's minipages. Keyval
options and styles can be used to determine their appearance in
an easy and consistent way. Includes options for paragraph
indentation and vertical alignment with respect to the visual
top and bottom margins.

%package -n texlive-genmpage-doc
Summary:        Documentation for genmpage
Version:        svn15878.0.3.1

Provides:       tex-genmpage-doc
AutoReqProv:    No

%description -n texlive-genmpage-doc
Documentation for genmpage

%package -n texlive-getfiledate
Provides:       tex-getfiledate = %{tl_version}
License:        LPPL
Summary:        Find the date of last modification of a file
Version:        svn16189.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etextools.sty), tex(ltxnew.sty), tex(xkeyval.sty), tex(xcolor.sty)
Requires:       tex(amssymb.sty), tex(boxedminipage.sty)
Provides:       tex(getfiledate.sty) = %{tl_version}

%description -n texlive-getfiledate
The package fetches from the system the date of last
modification or opening of an existing file, using the function
\pdffilemoddate (present in recent versions of PDFTeX); the
user may specify how the date is to be presented.

%package -n texlive-getfiledate-doc
Summary:        Documentation for getfiledate
Version:        svn16189.1.2

Provides:       tex-getfiledate-doc
AutoReqProv:    No

%description -n texlive-getfiledate-doc
Documentation for getfiledate

%package -n texlive-ginpenc
Provides:       tex-ginpenc = %{tl_version}
License:        LPPL
Summary:        Modification of inputenc for German
Version:        svn24980.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ginpenc.sty) = %{tl_version}

%description -n texlive-ginpenc
If the inputenc is used and German umlauts are input directly,
they are converted to the LICR representation \"a (etc.). This
breaks the sort algorithm of makeindex, for instance. Ginpenc
converts umlauts and the sharp-s to the short forms defined by
babel, e.g., "a instead, if the text is typeset in German.

%package -n texlive-ginpenc-doc
Summary:        Documentation for ginpenc
Version:        svn24980.1.0

Provides:       tex-ginpenc-doc
AutoReqProv:    No

%description -n texlive-ginpenc-doc
Documentation for ginpenc

%package -n texlive-gitinfo
Provides:       tex-gitinfo = %{tl_version}
License:        LPPL 1.3
Summary:        Access metadata from the git distributed version control system
Version:        svn34049.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etoolbox.sty), tex(kvoptions.sty), tex(xstring.sty)
Provides:       tex(gitinfo.sty) = %{tl_version}, tex(gitsetinfo.sty) = %{tl_version}

%description -n texlive-gitinfo
The package makes it possible to incorporate git version
control metadata into documents. For memoir users, the package
provides the means to tailor page headers and footers to use
the metadata. Note this version is now deprecated, but is kept
on the archive, pro tem, for continuity for existing users. All
new repositories should use gitinfo2.

%package -n texlive-gitinfo-doc
Summary:        Documentation for gitinfo
Version:        svn34049.1.0

Provides:       tex-gitinfo-doc
AutoReqProv:    No

%description -n texlive-gitinfo-doc
Documentation for gitinfo

%package -n texlive-gitinfo2
Provides:       tex-gitinfo2 = %{tl_version}
License:        LPPL 1.3
Summary:        Access metadata from the git distributed version control system
Version:        svn38913

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(xstring.sty), tex(etoolbox.sty), tex(eso-pic.sty)
Provides:       tex(gitexinfo.sty) = %{tl_version}, tex(gitinfo2.sty) = %{tl_version}

%description -n texlive-gitinfo2
The package makes it possible to incorporate git version
control metadata into documents. For memoir users, the package
provides the means to tailor page headers and footers to use
the metadata. gitinfo2 is a new release of gitinfo. The changes
to version 2 are not backward-compatible, and the package name
has been changed to avoid impact on existing users'
repositories. All new repositories should use this version of
the package.

%package -n texlive-gitinfo2-doc
Summary:        Documentation for gitinfo2
Version:        svn38913

Provides:       tex-gitinfo2-doc
AutoReqProv:    No

%description -n texlive-gitinfo2-doc
Documentation for gitinfo2

%package -n texlive-gloss
Provides:       tex-gloss = %{tl_version}
License:        LPPL
Summary:        Create glossaries using BibTeX
Version:        svn15878.1.5.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gloss.sty) = %{tl_version}

%description -n texlive-gloss
A glossary package using BibTeX with \cite replaced by \gloss.

%package -n texlive-gloss-doc
Summary:        Documentation for gloss
Version:        svn15878.1.5.2

Provides:       tex-gloss-doc
AutoReqProv:    No

%description -n texlive-gloss-doc
Documentation for gloss

%package -n texlive-glossaries-danish
Provides:       tex-glossaries-danish = %{tl_version}
License:        LPPL 1.3
Summary:        Danish language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-danish.ldf) = %{tl_version}

%description -n texlive-glossaries-danish
Danish language module for glossaries package.

%package -n texlive-glossaries-danish-doc
Summary:        Documentation for glossaries-danish
Version:        svn35665.1.0

Provides:       tex-glossaries-danish-doc
AutoReqProv:    No

%description -n texlive-glossaries-danish-doc
Documentation for glossaries-danish

%package -n texlive-glossaries-dutch
Provides:       tex-glossaries-dutch = %{tl_version}
License:        LPPL 1.3
Summary:        Dutch language module for glossaries package
Version:        svn35685.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-dutch.ldf) = %{tl_version}

%description -n texlive-glossaries-dutch
Dutch language module for glossariesr package.

%package -n texlive-glossaries-dutch-doc
Summary:        Documentation for glossaries-dutch
Version:        svn35685.1.1

Provides:       tex-glossaries-dutch-doc
AutoReqProv:    No

%description -n texlive-glossaries-dutch-doc
Documentation for glossaries-dutch

%package -n texlive-glossaries-english
Provides:       tex-glossaries-english = %{tl_version}
License:        LPPL 1.3
Summary:        English language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-english.ldf) = %{tl_version}

%description -n texlive-glossaries-english
English language module for glossariesr package.

%package -n texlive-glossaries-english-doc
Summary:        Documentation for glossaries-english
Version:        svn35665.1.0

Provides:       tex-glossaries-english-doc
AutoReqProv:    No

%description -n texlive-glossaries-english-doc
Documentation for glossaries-english

%package -n texlive-glossaries-french
Provides:       tex-glossaries-french = %{tl_version}
License:        LPPL 1.3
Summary:        French language module for glossaries package
Version:        svn42873
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(glossaries-french.ldf) = %{tl_version}

%description -n texlive-glossaries-french
French language module for glossaries package.

%package -n texlive-glossaries-french-doc
Summary:        Documentation for glossaries-french
Version:        svn42873
Provides:       tex-glossaries-french-doc
AutoReqProv:    No

%description -n texlive-glossaries-french-doc
Documentation for glossaries-french

%package -n texlive-glossaries-german
Provides:       tex-glossaries-german = %{tl_version}
License:        LPPL 1.3
Summary:        German language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-german.ldf) = %{tl_version}

%description -n texlive-glossaries-german
German language module for glossariesr package.

%package -n texlive-glossaries-german-doc
Summary:        Documentation for glossaries-german
Version:        svn35665.1.0

Provides:       tex-glossaries-german-doc
AutoReqProv:    No

%description -n texlive-glossaries-german-doc
Documentation for glossaries-german

%package -n texlive-glossaries-irish
Provides:       tex-glossaries-irish = %{tl_version}
License:        LPPL 1.3
Summary:        Irish language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-irish-noenc.ldf) = %{tl_version}
Provides:       tex(glossaries-irish-utf8.ldf) = %{tl_version}
Provides:       tex(glossaries-irish.ldf) = %{tl_version}

%description -n texlive-glossaries-irish
Irish language module for glossariesr package.

%package -n texlive-glossaries-irish-doc
Summary:        Documentation for glossaries-irish
Version:        svn35665.1.0

Provides:       tex-glossaries-irish-doc
AutoReqProv:    No

%description -n texlive-glossaries-irish-doc
Documentation for glossaries-irish

%package -n texlive-glossaries-italian
Provides:       tex-glossaries-italian = %{tl_version}
License:        LPPL 1.3
Summary:        Italian language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-italian.ldf) = %{tl_version}

%description -n texlive-glossaries-italian
Italian language module for glossaries package.

%package -n texlive-glossaries-italian-doc
Summary:        Documentation for glossaries-italian
Version:        svn35665.1.0

Provides:       tex-glossaries-italian-doc
AutoReqProv:    No

%description -n texlive-glossaries-italian-doc
Documentation for glossaries-italian

%package -n texlive-glossaries-magyar
Provides:       tex-glossaries-magyar = %{tl_version}
License:        LPPL 1.3
Summary:        Magyar language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-magyar-noenc.ldf) = %{tl_version}
Provides:       tex(glossaries-magyar-utf8.ldf) = %{tl_version}
Provides:       tex(glossaries-magyar.ldf) = %{tl_version}

%description -n texlive-glossaries-magyar
Magyar language module for glossariesr package.

%package -n texlive-glossaries-magyar-doc
Summary:        Documentation for glossaries-magyar
Version:        svn35665.1.0

Provides:       tex-glossaries-magyar-doc
AutoReqProv:    No

%description -n texlive-glossaries-magyar-doc
Documentation for glossaries-magyar

%package -n texlive-glossaries-polish
Provides:       tex-glossaries-polish = %{tl_version}
License:        LPPL 1.3
Summary:        Polish language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-polish-noenc.ldf) = %{tl_version}
Provides:       tex(glossaries-polish-utf8.ldf) = %{tl_version}
Provides:       tex(glossaries-polish.ldf) = %{tl_version}

%description -n texlive-glossaries-polish
Polish language module for glossariesr package.

%package -n texlive-glossaries-polish-doc
Summary:        Documentation for glossaries-polish
Version:        svn35665.1.0

Provides:       tex-glossaries-polish-doc
AutoReqProv:    No

%description -n texlive-glossaries-polish-doc
Documentation for glossaries-polish

%package -n texlive-glossaries-portuges
Provides:       tex-glossaries-portuges = %{tl_version}
License:        LPPL 1.3
Summary:        Portuges language module for glossaries package
Version:        svn36064.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-portuges-noenc.ldf) = %{tl_version}
Provides:       tex(glossaries-portuges-utf8.ldf) = %{tl_version}
Provides:       tex(glossaries-portuges.ldf) = %{tl_version}
Provides:       tex(glossaries-pt-BR.ldf) = %{tl_version}

%description -n texlive-glossaries-portuges
Portuges language module for glossaries package.

%package -n texlive-glossaries-portuges-doc
Summary:        Documentation for glossaries-portuges
Version:        svn36064.1.1

Provides:       tex-glossaries-portuges-doc
AutoReqProv:    No

%description -n texlive-glossaries-portuges-doc
Documentation for glossaries-portuges

%package -n texlive-glossaries-serbian
Provides:       tex-glossaries-serbian = %{tl_version}
License:        LPPL 1.3
Summary:        Serbian language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-serbian-noenc.ldf) = %{tl_version}
Provides:       tex(glossaries-serbian-utf8.ldf) = %{tl_version}
Provides:       tex(glossaries-serbian.ldf) = %{tl_version}

%description -n texlive-glossaries-serbian
Serbian language module for glossaries package.

%package -n texlive-glossaries-serbian-doc
Summary:        Documentation for glossaries-serbian
Version:        svn35665.1.0

Provides:       tex-glossaries-serbian-doc
AutoReqProv:    No

%description -n texlive-glossaries-serbian-doc
Documentation for glossaries-serbian

%package -n texlive-glossaries-spanish
Provides:       tex-glossaries-spanish = %{tl_version}
License:        LPPL 1.3
Summary:        Spanish language module for glossaries package
Version:        svn35665.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(glossaries-spanish-noenc.ldf) = %{tl_version}
Provides:       tex(glossaries-spanish-utf8.ldf) = %{tl_version}
Provides:       tex(glossaries-spanish.ldf) = %{tl_version}

%description -n texlive-glossaries-spanish
Spanish language module for glossaries package.

%package -n texlive-glossaries-spanish-doc
Summary:        Documentation for glossaries-spanish
Version:        svn35665.1.0

Provides:       tex-glossaries-spanish-doc
AutoReqProv:    No

%description -n texlive-glossaries-spanish-doc
Documentation for glossaries-spanish

%package -n texlive-gmdoc
Provides:       tex-gmdoc = %{tl_version}
License:        LPPL
Summary:        Documentation of LaTeX packages
Version:        svn21292.0.993

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(gmutils.sty), tex(xkeyval.sty), tex(xcolor.sty), tex(hyperref.sty)
Requires:       tex(gmiflink.sty), tex(gmverb.sty), tex(makeidx.sty), tex(multicol.sty)
Requires:       tex(tikz.sty), tex(lmodern.sty), tex(fontenc.sty), tex(geometry.sty)
Requires:       tex(trace.sty), tex(amsfonts.sty), tex(amsmath.sty), tex(amssymb.sty)
Provides:       tex(gmdoc.sty) = %{tl_version}, tex(gmdocc.cls) = %{tl_version}
Provides:       tex(gmoldcomm.sty) = %{tl_version}

%description -n texlive-gmdoc
A LaTeX package and an example class for documenting (La)TeX
packages, document classes, .dtx etc., providing hyperlinks.
The package is believed to be compatible with doc and permits
minimal markup of code (the macrocode environment is no longer
necessary). The package provides automatic detection of
definitions (detecting such things as \def, \newcommand,
\DeclareOption etc.). The package needs hyperref and the
author's three 'basic' packages: gmutils, gmverb and gmiflink.
As a bonus (and as an example of doc compatibility) driver
files are provided that may be used to typeset the LaTeX Base.

%package -n texlive-gmdoc-doc
Summary:        Documentation for gmdoc
Version:        svn21292.0.993

Provides:       tex-gmdoc-doc
AutoReqProv:    No

%description -n texlive-gmdoc-doc
Documentation for gmdoc

%package -n texlive-gmdoc-enhance
Provides:       tex-gmdoc-enhance = %{tl_version}
License:        LPPL
Summary:        Some enhancements to the gmdoc package
Version:        svn15878.v0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(gmdoc.sty)
Provides:       tex(gmdoc-enhance.sty) = %{tl_version}

%description -n texlive-gmdoc-enhance
This package provides some enhancements for the gmdoc package:
nicer formatting for multiple line inline comments, an ability
to "comment out" some code, and a macro to input other files in
"normal" LaTeX mode.

%package -n texlive-gmdoc-enhance-doc
Summary:        Documentation for gmdoc-enhance
Version:        svn15878.v0.2

Provides:       tex-gmdoc-enhance-doc
AutoReqProv:    No

%description -n texlive-gmdoc-enhance-doc
Documentation for gmdoc-enhance

%package -n texlive-gmiflink
Provides:       tex-gmiflink = %{tl_version}
License:        LPPL
Summary:        Simplify usage of \hypertarget and \hyperlink
Version:        svn15878.v0.97

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gmiflink.sty) = %{tl_version}

%description -n texlive-gmiflink
Three hyperref-based macros that simplify usage of \hypertarget
and \hyperlink: one argument instead of the same one twice.
Also \gmiflink and \gmifref which typeset plain text instead of
generating an error or printing '??' if there is no respective
hypertarget or label.

%package -n texlive-gmiflink-doc
Summary:        Documentation for gmiflink
Version:        svn15878.v0.97

Provides:       tex-gmiflink-doc
AutoReqProv:    No

%description -n texlive-gmiflink-doc
Documentation for gmiflink

%package -n texlive-gmutils
Provides:       tex-gmutils = %{tl_version}
License:        LPPL
Summary:        Support macros for other packages
Version:        svn24287.v0.996

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(graphicx.sty), tex(polski.sty)
Requires:       tex(xltxtra.sty), tex(multicol.sty), tex(calc.sty), tex(xkeyval.sty)
Provides:       tex(gmRCS.sty) = %{tl_version}, tex(gmampulex.sty) = %{tl_version}
Provides:       tex(gmbase.sty) = %{tl_version}, tex(gmcommand.sty) = %{tl_version}
Provides:       tex(gmenvir.sty) = %{tl_version}, tex(gmlogos.sty) = %{tl_version}
Provides:       tex(gmmeta.sty) = %{tl_version}, tex(gmmw.sty) = %{tl_version}
Provides:       tex(gmnotonlypream.sty) = %{tl_version}, tex(gmparts.sty) = %{tl_version}
Provides:       tex(gmrelsize.sty) = %{tl_version}, tex(gmtypos.sty) = %{tl_version}
Provides:       tex(gmurl.sty) = %{tl_version}, tex(gmutils.sty) = %{tl_version}

%description -n texlive-gmutils
Miscellaneous macros used by others of the author's packages.
Contents of the package: \newgif and other globals; \@ifnextcat
and \@ifXeTeX; \(Re)storeMacro(s) to override redefinitions;
\afterfi and friends; commands from relsize, etc.; "almost an
environment" or redefinition of \begin (\begin* doesn't check
if the argument environment is defined).

%package -n texlive-gmutils-doc
Summary:        Documentation for gmutils
Version:        svn24287.v0.996

Provides:       tex-gmutils-doc
AutoReqProv:    No

%description -n texlive-gmutils-doc
Documentation for gmutils

%package -n texlive-gmverb
Provides:       tex-gmverb = %{tl_version}
License:        LPPL
Summary:        A variant of LaTeX \verb, verbatim and shortvrb
Version:        svn24288.v0.98

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(gmcommand.sty), tex(xcolor.sty)
Provides:       tex(gmverb.sty) = %{tl_version}

%description -n texlive-gmverb
A redefinition of \verb and verbatim so that long lines are
breakable before \ and after { with % as 'hyphen'. Allows you
to define your own verbatim-like environments (subject to a
size limit) and allows you to declare any single character as a
shorthand as in the \MakeShortVerb command of the shortvrb
package of the LaTeX distribution. The package depends on the
gmutils package.

%package -n texlive-gmverb-doc
Summary:        Documentation for gmverb
Version:        svn24288.v0.98

Provides:       tex-gmverb-doc
AutoReqProv:    No

%description -n texlive-gmverb-doc
Documentation for gmverb

%package -n texlive-graphbox
Provides:       tex-graphbox = %{tl_version}
License:        LPPL 1.3
Summary:        Extend graphicx to improve placement of graphics
Version:        svn46360
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(graphicx.sty)
Provides:       tex(graphbox.sty) = %{tl_version}

%description -n texlive-graphbox
Graphbox is an extension of the standard graphicx LaTeX2e
package to allow the placement of graphics relative to the
"current position" using additional optional arguments of
\includegraphics. For example, changing the vertical alignment
is convenient for using graphics as elements of (mathematical)
formulae. Options for shifting, smashing and hiding the
graphics may be useful in support, for example, of the beamer
framework.

%package -n texlive-graphbox-doc
Summary:        Documentation for graphbox
Version:        svn46360
Provides:       tex-graphbox-doc
AutoReqProv:    No

%description -n texlive-graphbox-doc
Documentation for graphbox

%package -n texlive-graphicx-psmin
Provides:       tex-graphicx-psmin = %{tl_version}
License:        LPPL
Summary:        Reduce size of PostScript files by not repeating images
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty)
Provides:       tex(graphicx-psmin.sty) = %{tl_version}

%description -n texlive-graphicx-psmin
The package is an extension of the standard graphics bundle and
provides a way to include repeated PostScript graphics (ps,
eps) only once in a PostScript document. This leads to smaller
PostScript documents when having, for instance, a logo on every
page. The package only works when post-processed with dvips,
which should eb version 5.95b or later. The difference for a
resulting distilled PDF file is minimal (as Ghostscript and
Adobe Distiller only include a single copy of each graphics
file, anyway).

%package -n texlive-graphicx-psmin-doc
Summary:        Documentation for graphicx-psmin
Version:        svn15878.1.1

Provides:       tex-graphicx-psmin-doc
AutoReqProv:    No

%description -n texlive-graphicx-psmin-doc
Documentation for graphicx-psmin

%package -n texlive-graphicxbox
Provides:       tex-graphicxbox = %{tl_version}
License:        LPPL
Summary:        Insert a graphical image as a background
Version:        svn32630.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(graphicxbox.sty) = %{tl_version}

%description -n texlive-graphicxbox
The package defines two new commands \graphicxbox and
\fgraphicxbox, which are companions to \colorbox and \fcolorbox
of the Standard LaTeX color package. The \graphicxbox command
inserts a graphical image as a background rather than a
background color, while \fgraphicxbox does the same thing, but
also draws a colored frame around the box.

%package -n texlive-graphicxbox-doc
Summary:        Documentation for graphicxbox
Version:        svn32630.1.0

Provides:       tex-graphicxbox-doc
AutoReqProv:    No

%description -n texlive-graphicxbox-doc
Documentation for graphicxbox

%package -n texlive-grfpaste
Provides:       tex-grfpaste = %{tl_version}
License:        LPPL
Summary:        Include fragments of a dvi file
Version:        svn17354.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty)
Provides:       tex(grfpaste.sty) = %{tl_version}

%description -n texlive-grfpaste
Provides a mechanism to include fragments of dvi files with the
graphicx package, so that you can use \includegraphics to
include dvi files. The package requires the dvipaste program.

%package -n texlive-grfpaste-doc
Summary:        Documentation for grfpaste
Version:        svn17354.0.2

Provides:       tex-grfpaste-doc
AutoReqProv:    No

%description -n texlive-grfpaste-doc
Documentation for grfpaste

%package -n texlive-grid
Provides:       tex-grid = %{tl_version}
License:        LPPL
Summary:        Grid typesetting in LaTeX
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(keyval.sty)
Provides:       tex(grid.sty) = %{tl_version}

%description -n texlive-grid
The package helps to enables grid typesetting in double column
documents. Grid typesetting (vertical aligning of lines of text
in adjacent columns) is a difficult task in LaTeX, and the
present package is no more than an attempt to help users to
achieve it in a limited way. An example document, grid.tex, is
provided with simple instructions to typeset it using the
package. The package needs a lot more work: this is only a
beginning...

%package -n texlive-grid-doc
Summary:        Documentation for grid
Version:        svn15878.1.0

Provides:       tex-grid-doc
AutoReqProv:    No

%description -n texlive-grid-doc
Documentation for grid

%package -n texlive-grid-system
Provides:       tex-grid-system = %{tl_version}
License:        ASL 2.0
Summary:        Page organisation, modelled on CSS facilities
Version:        svn32981.0.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(xkeyval.sty), tex(ifthen.sty), tex(environ.sty)
Requires:       tex(forloop.sty)
Provides:       tex(grid-system.sty) = %{tl_version}

%description -n texlive-grid-system
The package provides the means for LaTeX to implement a grid
system as known from CSS grid systems. The facility is useful
for creating box layouts as used in brochures.

%package -n texlive-grid-system-doc
Summary:        Documentation for grid-system
Version:        svn32981.0.3.0

Provides:       tex-grid-system-doc
AutoReqProv:    No

%description -n texlive-grid-system-doc
Documentation for grid-system

%package -n texlive-gridset
Provides:       tex-gridset = %{tl_version}
License:        LPPL
Summary:        Grid, a.k.a. in-register, setting
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gridset.sty) = %{tl_version}

%description -n texlive-gridset
Grid setting -- also known as strict in-register setting -- is
something, that should be done for a lot of documents but is
not easy using LaTeX. The package helps to get the information
needed for grid setting. It does not implement auto grid
setting, but there is a command \vskipnextgrid, that moves to
the next grid position. This may be enough under some
circumstances, but in other circumstances it may fail. Thus
gridset is only one more step for grid setting, not a complete
solution.

%package -n texlive-gridset-doc
Summary:        Documentation for gridset
Version:        svn15878.0.1

Provides:       tex-gridset-doc
AutoReqProv:    No

%description -n texlive-gridset-doc
Documentation for gridset

%package -n texlive-gtl
Provides:       tex-gtl = %{tl_version}
License:        LPPL
Summary:        Manipulating generalized token lists
Version:        svn47304
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty)
Provides:       tex(gtl.sty) = %{tl_version}

%description -n texlive-gtl
The package provides tools for simple operations on lists of
tokens which are not necessarily balanced. It is in particular
used a lot in the unravel package, to go through tokens one at
a time rather than having to work with entire braced groups at
a time. The package requires an up-to-date l3kernel bundle.

%package -n texlive-gtl-doc
Summary:        Documentation for gtl
Version:        svn47304
Provides:       tex-gtl-doc
AutoReqProv:    No

%description -n texlive-gtl-doc
Documentation for gtl

%package -n texlive-guitlogo
Provides:       tex-guitlogo = %{tl_version}
License:        LPPL
Summary:        Macros for typesetting the GuIT logo
Version:        svn27458.0.9.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphics.sty), tex(url.sty), tex(xcolor.sty), tex(xkeyval.sty)
Provides:       tex(guit.cfg) = %{tl_version}, tex(guit.sty) = %{tl_version}

%description -n texlive-guitlogo
Guit provides some commands useful to correctly write the logo
of GUIT -- "Gruppo Utilizzatori Italiani di TeX" (Italian TeX
User Group), using the default document color or any other
color the user may ever choose, in conformity with logo's
scheme as seen on the Group web site
(http://www.guit.sssup.it). Likewise, commands are provided
that simplify the writing of GuIT acronym's complete expansion,
of the addresses of Group's internet site and public forum and
'GuITmeeting' logo. Optionally, using hyperref, the outputs of
the above cited commands can become hyperlinks to Group's site.
Documentation is available in Italian, only.

%package -n texlive-guitlogo-doc
Summary:        Documentation for guitlogo
Version:        svn27458.0.9.2

Provides:       tex-guitlogo-doc
AutoReqProv:    No

%description -n texlive-guitlogo-doc
Documentation for guitlogo

%package -n texlive-grundgesetze
Provides:       tex-grundgesetze = %{tl_version}
License:        GPLv2+
Summary:        Typeset Frege's Grundgesetze der Arithmetik
Version:        svn34439.1.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(bguq.sty)
Provides:       tex(grundgesetze.sty) = %{tl_version}

%description -n texlive-grundgesetze
The package defines maths mode commands for typesetting Gottlob
Frege's concept-script in the style of his "Grundgesetze der
Arithmetik" (Basic Laws of Arithmetic).

%package -n texlive-grundgesetze-doc
Summary:        Documentation for grundgesetze
Version:        svn34439.1.02

Provides:       tex-grundgesetze-doc
AutoReqProv:    No

%description -n texlive-grundgesetze-doc
Documentation for grundgesetze

%package -n texlive-garrigues
Provides:       tex-garrigues = %{tl_version}
License:        LPPL
Summary:        MetaPost macros for the reproduction of Garrigues' Easter nomogram
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-garrigues
Metapost macros for the reproduction of Garrigues' Easter
nomogram. These macros are described in Denis Roegel: An
introduction to nomography: Garrigues' nomogram for the
computation of Easter, TUGboat (volume 30, number 1, 2009,
pages 88-104)

%package -n texlive-garrigues-doc
Summary:        Documentation for garrigues
Version:        svn15878.0

Provides:       tex-garrigues-doc
AutoReqProv:    No

%description -n texlive-garrigues-doc
Documentation for garrigues

%package -n texlive-gmp
Provides:       tex-gmp = %{tl_version}
License:        LPPL 1.3
Summary:        Enable integration between MetaPost pictures and LaTeX
Version:        svn21691.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(graphicx.sty), tex(ifpdf.sty), tex(ifxetex.sty)
Requires:       tex(environ.sty)
Provides:       tex(gmp.sty) = %{tl_version}

%description -n texlive-gmp
The package allows integration between MetaPost pictures and
LaTeX. The main feature is that passing parameters to the
MetaPost pictures is possible and the picture code can be put
inside arguments to commands, including \newcommand.

%package -n texlive-gmp-doc
Summary:        Documentation for gmp
Version:        svn21691.1.0

Provides:       tex-gmp-doc
AutoReqProv:    No

%description -n texlive-gmp-doc
Documentation for gmp

%package -n texlive-gchords
Provides:       tex-gchords = %{tl_version}
License:        GPL+
Summary:        Typeset guitar chords
Version:        svn29803.1.20

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gchords.sty) = %{tl_version}

%description -n texlive-gchords
A LaTeX package for typesetting of guitar chord diagrams,
including options for chord names, finger numbers and
typesetting above lyrics. The bundle also includes a TCL script
(chordbox.tcl) that provides a graphical application which
creates LaTeX files that use gchords.sty.

%package -n texlive-gchords-doc
Summary:        Documentation for gchords
Version:        svn29803.1.20

Provides:       tex-gchords-doc
AutoReqProv:    No

%description -n texlive-gchords-doc
Documentation for gchords

%package -n texlive-gtrcrd
Provides:       tex-gtrcrd = %{tl_version}
License:        LPPL 1.3
Summary:        Add chords to lyrics
Version:        svn32484.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gtrcrd.sty) = %{tl_version}

%description -n texlive-gtrcrd
The package provides the means to specify guitar chords to be
played with each part of the lyrics of a song. The syntax of
the macros reduces the chance of failing to provide a chord
where one is needed, and the structure of the macros ensures
that the chord specification appears immediately above the
start of the lyric.

%package -n texlive-gtrcrd-doc
Summary:        Documentation for gtrcrd
Version:        svn32484.1.1

Provides:       tex-gtrcrd-doc
AutoReqProv:    No

%description -n texlive-gtrcrd-doc
Documentation for gtrcrd

%package -n texlive-guitar
Provides:       tex-guitar = %{tl_version}
License:        LPPL 1.3
Summary:        Guitar chords and song texts
Version:        svn32258.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(toolbox.sty)
Provides:       tex(guitar.sty) = %{tl_version}

%description -n texlive-guitar
(La)TeX macros for typesetting guitar chords over song texts.
The toolbox package is required. Note that this package only
places arbitrary TeX code over the lyrics. To typeset the
chords graphically (and not only by name), the author
recommends use of an additional package such as gchords by K.
Peeters.

%package -n texlive-guitar-doc
Summary:        Documentation for guitar
Version:        svn32258.1.6

Provides:       tex-guitar-doc
AutoReqProv:    No

%description -n texlive-guitar-doc
Documentation for guitar

%package -n texlive-guitarchordschemes
Provides:       tex-guitarchordschemes = %{tl_version}
License:        LPPL 1.3
Summary:        Guitar Chord and Scale Tablatures
Version:        svn41880
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(cnltx-base.sty)
Provides:       tex(guitarchordschemes.sty) = %{tl_version}

%description -n texlive-guitarchordschemes
This package provides two commands (\chordscheme and \scales).
With those commands it is possible to draw schematic diagrams
of guitar chord tablatures and scale tablatures. Both commands
know a range of options that allow wide customization of the
output. The package's drawing is done with the help of TikZ.

%package -n texlive-guitarchordschemes-doc
Summary:        Documentation for guitarchordschemes
Version:        svn41880
Provides:       tex-guitarchordschemes-doc
AutoReqProv:    No

%description -n texlive-guitarchordschemes-doc
Documentation for guitarchordschemes

%package -n texlive-getoptk
Provides:       tex-getoptk = %{tl_version}
License:        CeCILL-B
Summary:        Define macros with sophisticated options
Version:        svn23567.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(getoptk.tex) = %{tl_version}, tex(guide.tex) = %{tl_version}

%description -n texlive-getoptk
The package provides a means of defining macros whose options
are taken from a dictionary, which includes options which
themselves have arguments. The package was designed for use
with Plain TeX; its syntax derives from that of the \hbox,
\hrule, etc., TeX primitives.

%package -n texlive-getoptk-doc
Summary:        Documentation for getoptk
Version:        svn23567.1.0

Provides:       tex-getoptk-doc
AutoReqProv:    No

%description -n texlive-getoptk-doc
Documentation for getoptk

%package -n texlive-gfnotation
Provides:       tex-gfnotation = %{tl_version}
License:        GPLv3+
Summary:        Typeset Gottlob Frege's notation in plain TeX
Version:        svn37156.2.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(GFnotation.tex) = %{tl_version}

%description -n texlive-gfnotation
The package implements macros for plain TeX to typeset the
notation invented by Gottlob Frege in 1879 for his books
"Begriffsschrift" and "Grundgesetze der Arithmetik" (two
volumes). The output styles of both books are supported.

%package -n texlive-gfnotation-doc
Summary:        Documentation for gfnotation
Version:        svn37156.2.9

Provides:       tex-gfnotation-doc
AutoReqProv:    No

%description -n texlive-gfnotation-doc
Documentation for gfnotation

%package -n texlive-graphics-pln
Provides:       tex-graphics-pln = %{tl_version}
License:        LPPL
Summary:        LaTeX-style graphics for Plain TeX users
Version:        svn46363
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(autopict.sty) = %{tl_version}, tex(color.tex) = %{tl_version}
Provides:       tex(graphicx.tex) = %{tl_version}, tex(miniltx.tex) = %{tl_version}
Provides:       tex(picture.tex) = %{tl_version}, tex(psfrag.tex) = %{tl_version}

%description -n texlive-graphics-pln
The Plain TeX graphics package is mostly a thin shell around
the LaTeX graphicx and color packages, with support of the
LaTeX-isms in those packages provided by miniltx (which is the
largest part of the bundle). The bundle also contains a file
"picture.tex", which is a wrapper around the autopict.sty, and
provides the LaTeX picture mode to Plain TeX users.

%package -n texlive-graphics-pln-doc
Summary:        Documentation for graphics-pln
Version:        svn46363
Provides:       tex-graphics-pln-doc
AutoReqProv:    No

%description -n texlive-graphics-pln-doc
Documentation for graphics-pln

%package -n texlive-gaceta
Provides:       tex-gaceta = %{tl_version}
License:        LPPL
Summary:        A class to typeset La Gaceta de la RSME
Version:        svn15878.1.06

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(babel.sty), tex(graphicx.sty), tex(url.sty)
Requires:       tex(amsmath.sty), tex(amsthm.sty), tex(amssymb.sty)
Provides:       tex(gaceta.cls) = %{tl_version}

%description -n texlive-gaceta
The class will typeset papers for <<La Gaceta de la Real
Sociedad Matematica Espanola>>.

%package -n texlive-gaceta-doc
Summary:        Documentation for gaceta
Version:        svn15878.1.06

Provides:       tex-gaceta-doc
AutoReqProv:    No

%description -n texlive-gaceta-doc
Documentation for gaceta

%package -n texlive-gatech-thesis
Provides:       tex-gatech-thesis = %{tl_version}
License:        GPL+
Summary:        Georgia Institute of Technology thesis class
Version:        svn19886.1.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(gloss.sty), tex(index.sty), tex(multicol.sty), tex(calc.sty)
Provides:       tex(gatech-thesis-gloss.sty) = %{tl_version}
Provides:       tex(gatech-thesis-index.sty) = %{tl_version}
Provides:       tex(gatech-thesis-losa.sty) = %{tl_version}
Provides:       tex(gatech-thesis-patch.sty) = %{tl_version}
Provides:       tex(gatech-thesis.cls) = %{tl_version}

%description -n texlive-gatech-thesis
The output generated by using this class has been approved by
the Georgia Tech Office of Graduate Studies. It satisfies their
undocumented moving-target requirements in additional to the
actual documented requirements of the June 2002 Georgia Tech
Thesis Style Manual, as amended up to 2010.

%package -n texlive-gatech-thesis-doc
Summary:        Documentation for gatech-thesis
Version:        svn19886.1.8

Provides:       tex-gatech-thesis-doc
AutoReqProv:    No

%description -n texlive-gatech-thesis-doc
Documentation for gatech-thesis

%package -n texlive-gsemthesis
Provides:       tex-gsemthesis = %{tl_version}
License:        LPPL 1.3
Summary:        Geneva School of Economics and Management PhD thesis format
Version:        svn36244.0.9.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(geometry.sty), tex(hyperref.sty), tex(url.sty)
Provides:       tex(gsemthesis.cls) = %{tl_version}

%description -n texlive-gsemthesis
The class provides a PhD thesis template for the Geneva School
of Economics and Management (GSEM), University of Geneva,
Switzerland. The class provides utilities to easily set up the
cover page, the front matter pages, the page headers, etc.,
conformant to the official guidelines of the GSEM Faculty for
writing PhD dissertations.

%package -n texlive-gsemthesis-doc
Summary:        Documentation for gsemthesis
Version:        svn36244.0.9.4

Provides:       tex-gsemthesis-doc
AutoReqProv:    No

%description -n texlive-gsemthesis-doc
Documentation for gsemthesis

%package -n texlive-gzt
Provides:       tex-gzt = %{tl_version}
License:        LPPL 1.3
Summary:        Bundle of classes for "La Gazette des Mathematiciens"
Version:        svn47381
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(silence.sty), tex(xpatch.sty), tex(l3keys2e.sty), tex(xparse.sty)
Requires:       tex(standalone.sty), tex(datatool.sty), tex(fontenc.sty), tex(inputenc.sty)
Requires:       tex(fontspec.sty), tex(kpfonts.sty), tex(titlesec.sty), tex(multicol.sty)
Requires:       tex(graphicx.sty), tex(import.sty), tex(longtable.sty), tex(draftwatermark.sty)
Requires:       tex(adjustbox.sty), tex(zref-totpages.sty)
Requires:       tex(zref-xr.sty), tex(ragged2e.sty), tex(xspace.sty), tex(textcase.sty)
Requires:       tex(epigraph.sty), tex(csquotes.sty), tex(biblatex.sty), tex(array.sty)
Requires:       tex(booktabs.sty), tex(tabularx.sty), tex(nccparskip.sty), tex(multirow.sty)
Requires:       tex(varioref.sty), tex(mathtools.sty), tex(mathrsfs.sty), tex(esvect.sty)
Requires:       tex(everypage.sty), tex(translator.sty), tex(geometry.sty), tex(babel.sty)
Requires:       tex(eurosym.sty), tex(iflang.sty), tex(tableof.sty), tex(etoc.sty)
Requires:       tex(microtype.sty), tex(datetime.sty), tex(enumitem.sty), tex(fixltx2e.sty)
Requires:       tex(afterpage.sty), tex(xcolor.sty), tex(tikz.sty), tex(pgfplots.sty)
Requires:       tex(tcolorbox.sty), tex(tikzpagenodes.sty)
Requires:       tex(tkz-euclide.sty), tex(pagegrid.sty), tex(amsthm.sty), tex(thmtools.sty)
Requires:       tex(placeins.sty), tex(hyperref.sty), tex(bookmark.sty), tex(cleveref.sty)
Provides:       tex(gzt.cfg) = %{tl_version}, tex(gzt.cls) = %{tl_version}
Provides:       tex(gztarticle.cls) = %{tl_version}

%description -n texlive-gzt
This bundle provides the SMF classes gzt.cls and gztarticle.cls
(where SMF = Societe Mathematique de France) for the French
journal "La Gazette des Mathematiciens". gztarticle.cls allows
for a close reproduction of the layout of the "Gazette" and
provides a number of environments, especially for typesetting
mathematic formulas.

%package -n texlive-gzt-doc
Summary:        Documentation for gzt
Version:        svn47381
Provides:       tex-gzt-doc
AutoReqProv:    No

%description -n texlive-gzt-doc
Documentation for gzt

%package -n texlive-galois
Provides:       tex-galois = %{tl_version}
License:        LPPL
Summary:        Typeset Galois connections
Version:        svn15878.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(galois.sty) = %{tl_version}

%description -n texlive-galois
The package deals with connections in two-dimensional style,
optionally in colour.

%package -n texlive-galois-doc
Summary:        Documentation for galois
Version:        svn15878.1.5

Provides:       tex-galois-doc
AutoReqProv:    No

%description -n texlive-galois-doc
Documentation for galois

%package -n texlive-gastex
Provides:       tex-gastex = %{tl_version}
License:        LPPL
Summary:        Graphs and Automata Simplified in TeX
Version:        svn15878.2.8

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(trig.sty)
Provides:       tex(gastex.sty) = %{tl_version}

%description -n texlive-gastex
GasTeX is a set of LaTeX macros which enable the user to draw
graphs, automata, nets, diagrams, etc., very easily, in the
LaTeX picture environment. The package offers no documentation
(per se), but offers a couple of example files in the
distribution, and more on its home page. GasTeX generates its
own PostScript code, and therefore doesn't work directly under
PDFLaTeX.

%package -n texlive-gastex-doc
Summary:        Documentation for gastex
Version:        svn15878.2.8

Provides:       tex-gastex-doc
AutoReqProv:    No

%description -n texlive-gastex-doc
Documentation for gastex

%package -n texlive-gene-logic
Provides:       tex-gene-logic = %{tl_version}
License:        Crossword
Summary:        Typeset logic formulae, etc
Version:        svn15878.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gn-logic14.sty) = %{tl_version}

%description -n texlive-gene-logic
The package provides a facility to typeset certain logic
formulae. It provides an environment like eqnarray, a
newtheorem-like environment (NewTheorem), and several macros.

%package -n texlive-gene-logic-doc
Summary:        Documentation for gene-logic
Version:        svn15878.1.4

Provides:       tex-gene-logic-doc
AutoReqProv:    No

%description -n texlive-gene-logic-doc
Documentation for gene-logic

%package -n texlive-ghsystem
Provides:       tex-ghsystem = %{tl_version}
License:        LPPL 1.3
Summary:        Globally harmonised system of chemical (etc) naming
Version:        svn41714
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(translations.sty)
Requires:       tex(siunitx.sty), tex(graphicx.sty), tex(longtable.sty), tex(ifpdf.sty)
Provides:       tex(ghsystem.sty) = %{tl_version}, tex(ghsystem_english.def) = %{tl_version}
Provides:       tex(ghsystem_german.def) = %{tl_version}
Provides:       tex(ghsystem_italian-2-slash.def) = %{tl_version}
Provides:       tex(ghsystem_italian.def) = %{tl_version}
Provides:       tex(ghsystem_langtemplate.def) = %{tl_version}
Provides:       tex(ghsystem_ngerman.def) = %{tl_version}
Provides:       tex(ghsystem_spanish.def) = %{tl_version}
Provides:       tex(ghsystem_acid-8.tex) = %{tl_version}
Provides:       tex(ghsystem_acid.tex) = %{tl_version}, tex(ghsystem_aqpol.tex) = %{tl_version}
Provides:       tex(ghsystem_bottle-2-black.tex) = %{tl_version}
Provides:       tex(ghsystem_bottle-2-white.tex) = %{tl_version}
Provides:       tex(ghsystem_bottle.tex) = %{tl_version}
Provides:       tex(ghsystem_exclam.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-1.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-2.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-3.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-4.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-5.tex) = %{tl_version}
Provides:       tex(ghsystem_explos-6.tex) = %{tl_version}
Provides:       tex(ghsystem_explos.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-2-black.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-2-white.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-3-black.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-3-white.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-4-1.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-4-2.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-4-3-black.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-4-3-white.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-5-2-black.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-5-2-white.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-O-5-1.tex) = %{tl_version}
Provides:       tex(ghsystem_flame-O.tex) = %{tl_version}
Provides:       tex(ghsystem_flame.tex) = %{tl_version}, tex(ghsystem_health.tex) = %{tl_version}
Provides:       tex(ghsystem_skull-2.tex) = %{tl_version}
Provides:       tex(ghsystem_skull-6.tex) = %{tl_version}
Provides:       tex(ghsystem_skull.tex) = %{tl_version}

%description -n texlive-ghsystem
The package provides the means to typeset all the hazard and
precautionary statements and pictograms in a straightforward
way. The statements are taken from EU regulation 1272/2008.

%package -n texlive-ghsystem-doc
Summary:        Documentation for ghsystem
Version:        svn41714
Provides:       tex-ghsystem-doc
AutoReqProv:    No

%description -n texlive-ghsystem-doc
Documentation for ghsystem

%package -n texlive-gu
Provides:       tex-gu = %{tl_version}
License:        LPPL
Summary:        Typeset crystallographic group-subgroup-schemes
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(array.sty), tex(tabularx.sty), tex(pict2e.sty), tex(calc.sty)
Requires:       tex(fp.sty), tex(ifthen.sty)
Provides:       tex(gu.sty) = %{tl_version}

%description -n texlive-gu
The package simplifies typesetting of simple crystallographic
group-subgroup-schemes in the Barnighausen formalism. It
defines a new environment stammbaum, wherein all elements of
the scheme are defined. Afterwards all necessary dimensions are
calculated and the scheme is drawn. Currently two steps of
symmetry reduction are supported.

%package -n texlive-gu-doc
Summary:        Documentation for gu
Version:        svn15878.0

Provides:       tex-gu-doc
AutoReqProv:    No

%description -n texlive-gu-doc
Documentation for gu

%package -n texlive-getitems-doc
Provides:       tex-getitems-doc = %{tl_version}
License:        LPPL
Summary:        doc files of getitems
Version:        svn39365

AutoReqProv:    No

%description -n texlive-getitems-doc
Documentation for getitems

%package -n texlive-getitems
Provides:       tex-getitems = %{tl_version}
License:        LPPL
Summary:        Gathering items from a list-like environment
Version:        svn39365

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(getitems.sty) = %{tl_version}

%description -n texlive-getitems
This package provides a \gatheritems command to parse a list of
data separated by \item tokens. This makes it easier to define
custom environments which structure their data in the same way
that itemize or enumerate do.

%package -n texlive-gitlog-doc
Provides:       tex-gitlog-doc = %{tl_version}
License:        LPPL
Summary:        doc files of gitlog
Version:        svn38932

AutoReqProv:    No

%description -n texlive-gitlog-doc
Documentation for gitlog

%package -n texlive-gitlog
Provides:       tex-gitlog = %{tl_version}
License:        LPPL
Summary:        Typesetting git changelogs
Version:        svn38932

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gitlog.sty) = %{tl_version}

%description -n texlive-gitlog
This package allows git change log history to be incorporated
into LaTeX documents; the log data is obtained from the git
distributed version control system. The current release
(0.0.beta) is a proof-of-concept release to allow users an
early evaluation and to attract ideas and support. Requests and
suggestions, as well as code contributions are welcome.

%package -n texlive-glossaries-extra-doc
Provides:       tex-glossaries-extra-doc = %{tl_version}
License:        LPPL
Summary:        doc files of glossaries-extra
Version:        svn48401
AutoReqProv:    No

%description -n texlive-glossaries-extra-doc
Documentation for glossaries-extra

%package -n texlive-glossaries-extra
Provides:       tex-glossaries-extra = %{tl_version}
License:        LPPL
Summary:        An extension to the glossaries package
Version:        svn48401
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(glossaries-extra.sty) = %{tl_version}
Provides:       tex(glossaries-extra-stylemods.sty) = %{tl_version}

%description -n texlive-glossaries-extra
This package provides improvements and extra features to the
glossaries package. Some of the default glossaries.sty
behaviour is changed by glossaries-extra.sty. See the user
manual glossaries-extra-manual.pdf for further details.

%package -n texlive-gloss-occitan-doc
Provides:       tex-gloss-occitan-doc = %{tl_version}
License:        LPPL
Summary:        doc files of gloss-occitan
Version:        svn39609

AutoReqProv:    No

%description -n texlive-gloss-occitan-doc
Documentation for gloss-occitan

%package -n texlive-gloss-occitan
Provides:       tex-gloss-occitan = %{tl_version}
License:        LPPL
Summary:        Polyglossia support for Occitan
Version:        svn39609

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gloss-occitan.ldf) = %{tl_version}

%description -n texlive-gloss-occitan
Occitan language description file for polyglossia

%package -n texlive-gobble-doc
Provides:       tex-gobble-doc = %{tl_version}
License:        LPPL
Summary:        doc files of gobble
Version:        svn40936

AutoReqProv:    No

%description -n texlive-gobble-doc
Documentation for gobble

%package -n texlive-gobble
Provides:       tex-gobble = %{tl_version}
License:        LPPL
Summary:        More gobble macros for PlainTeX and LaTeX
Version:        svn40936

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gobble.sty) = %{tl_version}, tex(gobble-user.sty) = %{tl_version}
Provides:       tex(gobble.tex) = %{tl_version}

%description -n texlive-gobble
The LaTeX package gobble includes several gobble macros not
included in the LaTeX kernel. These macros remove a number of
arguments after them, a feature regulary used inside other
macros. This includes gobble macros for optional arguments. The
LaTeX package gobble-user provides these macros at the user
level, i.e. using names without @ so that these can be used
without \makeatletter and \makeatother. The same macros are
provided inside .tex files for use with plain-TeX or other TeX
formats. However, the gobble macros for optional macros require
\@ifnextchar to be defined.

%package -n texlive-gradstudentresume-doc
Provides:       tex-gradstudentresume-doc = %{tl_version}
License:        LPPL
Summary:        doc files of gradstudentresume
Version:        svn38832

AutoReqProv:    No

%description -n texlive-gradstudentresume-doc
Documentation for gradstudentresume

%package -n texlive-gradstudentresume
Provides:       tex-gradstudentresume = %{tl_version}
License:        LPPL
Summary:        A generic template for graduate student resumes
Version:        svn38832

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(gradstudentresume.cls) = %{tl_version}

%description -n texlive-gradstudentresume
The package offers a template for graduate students writing an
academic CV. The goal is to create a flexible template that can
be customized based on each specific individual's needs.

%package -n texlive-graphics-cfg-doc
Provides:       tex-graphics-cfg-doc = %{tl_version}
License:        CC-0
Summary:        doc files of graphics-cfg
Version:        svn40269

AutoReqProv:    No

%description -n texlive-graphics-cfg-doc
Documentation for graphics-cfg

%package -n texlive-graphics-cfg
Provides:       tex-graphics-cfg = %{tl_version}
License:        Public Domain
Summary:        Sample configuration files for LaTeX color and graphics
Version:        svn40269

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(color.cfg) = %{tl_version}, tex(graphics.cfg) = %{tl_version}

%description -n texlive-graphics-cfg
This bundle includes color.cfg and graphics.cfg files that set
default "driver" options for the color and graphics packages.
It contains support for defaulting the new LuaTeX option which
was added to graphics and color in the 2016-02-01 release. The
LuaTeX option is only used for LuaTeX versions from 0.87, older
versions use the pdfTeX option as before.

%package -n texlive-greektonoi-doc
Provides:       tex-greektonoi-doc = %{tl_version}
License:        GPLv3
Summary:        doc files of greektonoi
Version:        svn39419

AutoReqProv:    No

%description -n texlive-greektonoi-doc
Documentation for greektonoi

%package -n texlive-greektonoi
Provides:       tex-greektonoi = %{tl_version}
License:        GPLv3
Summary:        Facilitates writing/editing of multiaccented greek
Version:        svn39419

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(greektonoi.sty) = %{tl_version}, tex(greektonoi.map) = %{tl_version}

%description -n texlive-greektonoi
The greektonoi mapping extends the betababel package or the
babel polutonikogreek option to provide a simple way to insert
ancient Greek texts with diacritical characters into your
document using a similar method to the commonly used Beta Code
transliteration, but with much more freedom. It is designed
especially for the XeTeX engine and it could also be used for
fast and easy modification of monotonic greek texts to
polytonic. The output text is natively encoded in Unicode, so
it can be reused in any possible way. The greektonoi package
provides, in addition to inserting greek accents and
breathings, many other symbols used in greek numbers and
arithmetic or in the greek archaic period. It could be used
with greektonoi mapping or indepedently.

%package -n texlive-graphics-def
Provides:       tex-graphics-def = %{tl_version}
License:        LPPL
Summary:        Colour and graphics option files
Version:        svn46267
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       texlive-pdftex-def = %{tl_version}
Obsoletes:      texlive-pdftex-def <= 6:svn22653.0.06d
Provides:       texlive-dvipdfmx-def = %{tl_version}
Obsoletes:      texlive-dvipdfmx-def <= 6:svn40328
Provides:       texlive-dvisvgm-def = %{tl_version}
Obsoletes:      texlive-dvisvgm-def <= 6:svn41011
Provides:       texlive-luatex-def = %{tl_version}
Obsoletes:      texlive-luatex-def <= 6:svn41466
Provides:       texlive-xetex-def = %{tl_version}
Obsoletes:      texlive-xetex-def <= 6:svn40327
Provides:       tex(dvipdfmx.def) = %{tl_version}, tex(dvips.def) = %{tl_version}
Provides:       tex(dvisvgm.def) = %{tl_version}, tex(luatex.def) = %{tl_version}
Provides:       tex(pdftex.def) = %{tl_version}, tex(xetex.def) = %{tl_version}

%description -n texlive-graphics-def
This bundle is a combined distribution consisting of dvips.def,
pdftex.def, luatex.def, xetex.def, dvipdfmx.def, and
dvisvgm.def driver option files for the LaTeX graphics and
color packages. It is hoped that by combining their source
repositories at https://github.com/latex3/graphics-def it will
be easier to coordinate updates.

%package -n texlive-gitfile-info
Summary:        Get git metadata for a specific file
Version:        svn41693
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(gitfile-info.sty) = %{tl_version}

%description -n texlive-gitfile-info
If you are using git to control versions of LaTeX-files, you
may want to show yourself or other users or devs the current
version of the file, information about the author and last
edited date. All packages for git known make that kind of
information available for the whole repository. But sometimes
you have a lot of files within the same repository in different
versions, from different authors etc. Perhaps you also split up
a big project in small files and want to show within the
document who had edited what. This package gives you the
opportunity to do so.

%package -n texlive-gofonts
Summary:        GoSans and GoMono fonts with LaTeX support
Version:        svn43726
License:        BSD and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(go_dpz6hk.enc) = %{tl_version}, tex(go_ie7fbt.enc) = %{tl_version}
Provides:       tex(go_t66sex.enc) = %{tl_version}, tex(go_yzw7so.enc) = %{tl_version}
Provides:       tex(go.map) = %{tl_version}, tex(Go-Bold-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Go-Bold-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Go-Bold-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Go-Bold-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Go-Bold-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Go-Bold-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Go-Bold-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Go-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Go-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Go-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Go-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Go-Bold-tlf-t1.tfm) = %{tl_version}, tex(Go-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Go-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Go-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Go-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Go-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Go-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Go-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Go-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Go-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Go-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Go-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Go-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Go-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Go-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Go-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Go-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(GoMono-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-tlf-ly1.tfm) = %{tl_version}, tex(GoMono-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(GoMono-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-tlf-t1.tfm) = %{tl_version}, tex(GoMono-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GoMono-tlf-ts1.tfm) = %{tl_version}, tex(GoSmallcaps-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-t1.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Go-Bold-Italic.ttf) = %{tl_version}, tex(Go-Bold.ttf) = %{tl_version}
Provides:       tex(Go-Medium-Italic.ttf) = %{tl_version}
Provides:       tex(Go-Medium.ttf) = %{tl_version}, tex(Go-Regular-Italic.ttf) = %{tl_version}
Provides:       tex(Go-Regular.ttf) = %{tl_version}, tex(GoMono-Bold-Italic.ttf) = %{tl_version}
Provides:       tex(GoMono-Bold.ttf) = %{tl_version}, tex(GoMono-Regular-Italic.ttf) = %{tl_version}
Provides:       tex(GoMono-Regular.ttf) = %{tl_version}, tex(GoSmallcaps-Italic.ttf) = %{tl_version}
Provides:       tex(GoSmallcaps.ttf) = %{tl_version}, tex(Go-Bold-Italic.pfb) = %{tl_version}
Provides:       tex(Go-Bold.pfb) = %{tl_version}, tex(Go-Medium-Italic.pfb) = %{tl_version}
Provides:       tex(Go-Medium.pfb) = %{tl_version}, tex(Go-Regular-Italic.pfb) = %{tl_version}
Provides:       tex(Go-Regular.pfb) = %{tl_version}, tex(GoMono-Bold-Italic.pfb) = %{tl_version}
Provides:       tex(GoMono-Bold.pfb) = %{tl_version}, tex(GoMono-Regular-Italic.pfb) = %{tl_version}
Provides:       tex(GoMono-Regular.pfb) = %{tl_version}, tex(GoSmallcaps-Italic.pfb) = %{tl_version}
Provides:       tex(GoSmallcaps.pfb) = %{tl_version}, tex(GoMono.sty) = %{tl_version}
Provides:       tex(GoSans.sty) = %{tl_version}, tex(Go-Bold-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Go-Bold-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Go-Bold-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Go-Bold-tlf-ly1.vf) = %{tl_version}, tex(Go-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Go-Bold-tlf-ts1.vf) = %{tl_version}, tex(Go-Medium-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Go-Medium-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Go-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Go-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(Go-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Go-Regular-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Go-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Go-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Go-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(GoMono-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(GoMono-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(GoMono-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(GoMono-tlf-ly1.vf) = %{tl_version}, tex(GoMono-tlf-t1.vf) = %{tl_version}
Provides:       tex(GoMono-tlf-ts1.vf) = %{tl_version}, tex(GoSmallcaps-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(GoSmallcaps-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(GoSmallcaps-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-ly1.vf) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-t1.vf) = %{tl_version}
Provides:       tex(GoSmallcaps-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Go-TLF.fd) = %{tl_version}, tex(LY1GoMono-TLF.fd) = %{tl_version}
Provides:       tex(OT1Go-TLF.fd) = %{tl_version}, tex(OT1GoMono-TLF.fd) = %{tl_version}
Provides:       tex(T1Go-TLF.fd) = %{tl_version}, tex(T1GoMono-TLF.fd) = %{tl_version}
Provides:       tex(TS1Go-TLF.fd) = %{tl_version}, tex(TS1GoMono-TLF.fd) = %{tl_version}

%description -n texlive-gofonts
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the GoSans and GoMono families of fonts designed by
the Bigelow & Holmes foundry for the Go project. GoSans is
available in three weights: Regular, Medium, and Bold (with
corresponding italics). GoMono is available in regular and
bold, with italics. Notes on the design may be found at
https://blog.golang.org/go-fonts.

%package -n texlive-grant
Summary:        Classes for formatting federal grant proposals.
Version:        svn41905
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(grant-arl.cls) = %{tl_version}, tex(grant-darpa.cls) = %{tl_version}
Provides:       tex(grant-doe.cls) = %{tl_version}, tex(grant-nih.cls) = %{tl_version}
Provides:       tex(grant-nrl.cls) = %{tl_version}, tex(grant-nsf.cls) = %{tl_version}
Provides:       tex(grant-onr.cls) = %{tl_version}, tex(grant.cls) = %{tl_version}

%description -n texlive-grant
LaTeX classes for formatting federal grant proposals: grant:
Base class for formatting grant proposals grant-arl: Army
Research Laboratory grant-darpa: Defense Advanced Research
Projects Agency grant-doe: Department of Energy grant-nih:
National Institutes of Health grant-nrl: Naval Research
Laboratory grant-nsf: National Science Foundation grant-onr:
Office of Naval Research

%package -n texlive-grayhints
Summary:        Produce 'gray hints' to a variable text field
Version:        svn43561
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(grayhints.sty) = %{tl_version}

%description -n texlive-grayhints
The package provides JavaScript code snippets to create 'gray
hints'. Gray hints, as the author terms them, are text that
appears initially in a text field that gives a short hint as to
what the contents of the text field should be. For example, a
text field might contain the hint 'First Name', or a date field
might read 'yyyy/mm/dd'. As soon as the field comes into focus,
the hint disappears. It reappears when the field is blurred and
the user did not enter any text into the field. The package
works for dvips/Distiller, pdfLaTeX, LuaLaTeX, and XeLaTeX.

%package -n texlive-gtrlib-largetrees
Summary:        Library for genealogytree package aiming at large trees
Version:        svn43279
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(gtrlib.largetrees.code.tex) = %{tl_version}
Provides:       tex(gtrlib.largetrees.sty) = %{tl_version}

%description -n texlive-gtrlib-largetrees
The main goal of the gtrlib.largetrees package is to offer
additional database fields and formats for the genealogytree
package, particularly for typesetting large trees.

%package -n texlive-gatherenum
Summary:        A crossover of align* and enumerate
Version:        svn48051
License:        GPLv3+
Requires:       texlive-base texlive-kpathsea, tex(enumitem.sty)
Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(gatherenum.sty) = %{tl_version}

%description -n texlive-gatherenum
This package (ab)uses the inline enumeration capabilities of
enumitem to add a "displayed" enumeration mode, triggered by
adding 'gathered' to the key-value option list of the enumerate
environment. The end result is similar to a regular enumerate
environment wrapped in a multicols environment, with the
following advantages: Gathered enumerate can pack items
depending on their actual width rather than a fixed, constant
number per line. Gathered enumeration fills items in a
line-major order (instead of column-major order), which my
students found less confusing. YMMV. The package depends on
enumitem, expl3, and xparse,

%package -n texlive-gbt7714
Summary:        BibTeX implementation of China's bibliography style standard GB/T 7714-2015
Version:        svn48352
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(gbt7714-2005-plain.bst) = %{tl_version}
Provides:       tex(gbt7714-2005-unsrt.bst) = %{tl_version}
Provides:       tex(gbt7714-plain.bst) = %{tl_version}, tex(gbt7714-unsrt.bst) = %{tl_version}
Provides:       tex(gbt7714.sty) = %{tl_version}

%description -n texlive-gbt7714
The package provides a BibTeX implementation for the Chinese
national bibliography style standard GB/T 7714-2015. It
consists of two bst files for numerical and author-year styles
and a LaTeX package which provides the citation style defined
in the standard. It also support automatic language
recognization (Chinese and English) for each biblilography
entry and is designed to be fully compatible with natbib.

%package -n texlive-gentombow
Summary:        Generate Japanese-style crop marks
Version:        svn48449
License:        BSD
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bounddvi.sty) = %{tl_version}, tex(gentombow.sty) = %{tl_version}
Provides:       tex(pxgentombow.sty) = %{tl_version}

%description -n texlive-gentombow
This bundle provides a LaTeX package for generating
Japanese-style crop marks (called 'tombow' in Japanese) for
practical use in self-publishing. The bundle contains the
following packages: gentombow.sty: Generate crop marks (called
'tombow' in Japanese) for practical use in self-publishing. It
provides the core 'tombow' feature if not available.
pxgentombow.sty: Superseded by gentombow.sty; kept for
compatibility only. bounddvi.sty: Set papersize special to DVI
file. Can be used on LaTeX/pLaTeX/upLaTeX (with DVI output
mode) with dvips or dvipdfmx drivers.

%package -n texlive-gfsneohellenicmath
Summary:        A Greek math font in the Neo-Hellenic style
Version:        svn46869
License:        OFL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(gfsneohellenicot.sty) = %{tl_version}
Provides:       tex(GFSNeohellenicMath.otf) = %{tl_version}

%description -n texlive-gfsneohellenicmath
The GFSNeohellenic font, a historic font first designed by
Victor Scholderer, and digitized by George Matthiopoulos of the
Greek Font Society (GFS), now has native support for
Mathematics. The project was commissioned to GFS by the
Department of Mathematics of the University of the Aegean,
Samos, Greece. The Math Table was constructed by the
Mathematics Professor A. Tsolomitis. A useful application is in
beamer documents since this is a Sans Math font. The
GFSNeohellenic fontfamily supports many languages (including
Greek), and it is distributed (both text and math) under the
OFL license.

%package -n texlive-glossaries-finnish
Summary:        Finnish language module for glossaries package
Version:        svn45604
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(glossaries-finnish-ascii.ldf) = %{tl_version}
Provides:       tex(glossaries-finnish-utf8.ldf) = %{tl_version}
Provides:       tex(glossaries-finnish.ldf) = %{tl_version}

%description -n texlive-glossaries-finnish
Finnish language module for glossaries package.

%package -n texlive-gotoh
Summary:        An implementation of the Gotoh sequence alignment algorithm
Version:        svn44764
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(gotoh.sty) = %{tl_version}

%description -n texlive-gotoh
This package calculates biological sequence alignment with the
Gotoh algorithm. The package also provides an interface to
control various settings including algorithm parameters.

%package -n texlive-graph35
Summary:        Draw keys and screen items of several Casio calculators
Version:        svn47522
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(graph35.sty) = %{tl_version}, tex(graph35-pixelart.sty) = %{tl_version}
Provides:       tex(graph35-keys.sty) = %{tl_version}

%description -n texlive-graph35
This package defines commands to draw the Casio Graph 35 /
fx-9750GII calculator (and other models). It can draw the whole
calculator, or parts of it (individual keys, part of the
screen, etc.). It was written to typeset documents instructing
students how to use their calculator.

%package -n texlive-graphicxpsd
Summary:        Adobe Photoshop Data format (PSD) support for graphicx package
Version:        svn46477
License:        MIT
Requires:       texlive-base texlive-kpathsea, ImageMagick
Provides:       tex(graphicxpsd.sty) = %{tl_version}

%description -n texlive-graphicxpsd
This package provides Adobe Photoshop Data format (PSD) support
for graphicx package with sips (Darwin/macOS) / convert
(ImageMagick) command.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="arkandis/gillius public/gfsartemisia public/gfsbaskerville \
public/gfsbodoni public/gfscomplutum public/gfsdidot \
public/gfsneohellenic public/gfsporson public/gfssolomos public/gnu-freefont"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-garuda-c90
%{_texdir}/texmf-dist/dvips/garuda-c90/
%{_texdir}/texmf-dist/fonts/map/dvips/garuda-c90/
%{_texdir}/texmf-dist/fonts/tfm/public/garuda-c90/

%files -n texlive-geometry
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/geometry/

%files -n texlive-geometry-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/geometry/

%files -n texlive-graphics
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/graphics/

%files -n texlive-graphics-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/graphics/

%files -n texlive-geschichtsfrkl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/geschichtsfrkl/

%files -n texlive-geschichtsfrkl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/geschichtsfrkl/

%files -n texlive-genealogy
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/genealogy/
%{_texdir}/texmf-dist/fonts/tfm/public/genealogy/

%files -n texlive-genealogy-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/genealogy/

%files -n texlive-gentium-tug
%license other-free.txt
%{_texdir}/texmf-dist/fonts/afm/public/gentium-tug/
%{_texdir}/texmf-dist/fonts/enc/dvips/gentium-tug/
%{_texdir}/texmf-dist/fonts/map/dvips/gentium-tug/
%{_texdir}/texmf-dist/fonts/map/pdftex/gentium-tug/
%{_texdir}/texmf-dist/fonts/tfm/public/gentium-tug/
%{_texdir}/texmf-dist/fonts/truetype/public/gentium-tug/
%{_texdir}/texmf-dist/fonts/type1/public/gentium-tug/
%{_texdir}/texmf-dist/tex/context/third/gentium-tug/
%{_texdir}/texmf-dist/tex/latex/gentium-tug/

%files -n texlive-gentium-tug-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/fonts/gentium-tug/

%files -n texlive-gfsartemisia
%{_datadir}/fonts/gfsartemisia
%{_texdir}/texmf-dist/fonts/afm/public/gfsartemisia/
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsartemisia/
%{_texdir}/texmf-dist/fonts/map/dvips/gfsartemisia/
%{_texdir}/texmf-dist/fonts/opentype/public/gfsartemisia/
%{_texdir}/texmf-dist/fonts/tfm/public/gfsartemisia/
%{_texdir}/texmf-dist/fonts/type1/public/gfsartemisia/
%{_texdir}/texmf-dist/fonts/vf/public/gfsartemisia/
%{_texdir}/texmf-dist/tex/latex/gfsartemisia/

%files -n texlive-gfsartemisia-doc
%{_texdir}/texmf-dist/doc/fonts/gfsartemisia/

%files -n texlive-gfsbodoni
%{_datadir}/fonts/gfsbodoni
%{_texdir}/texmf-dist/fonts/afm/public/gfsbodoni/
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbodoni/
%{_texdir}/texmf-dist/fonts/map/dvips/gfsbodoni/
%{_texdir}/texmf-dist/fonts/opentype/public/gfsbodoni/
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbodoni/
%{_texdir}/texmf-dist/fonts/type1/public/gfsbodoni/
%{_texdir}/texmf-dist/fonts/vf/public/gfsbodoni/
%{_texdir}/texmf-dist/tex/latex/gfsbodoni/

%files -n texlive-gfsbodoni-doc
%{_texdir}/texmf-dist/doc/fonts/gfsbodoni/

%files -n texlive-gfscomplutum
%{_datadir}/fonts/gfscomplutum
%{_texdir}/texmf-dist/fonts/afm/public/gfscomplutum/
%{_texdir}/texmf-dist/fonts/enc/dvips/gfscomplutum/
%{_texdir}/texmf-dist/fonts/map/dvips/gfscomplutum/
%{_texdir}/texmf-dist/fonts/opentype/public/gfscomplutum/
%{_texdir}/texmf-dist/fonts/tfm/public/gfscomplutum/
%{_texdir}/texmf-dist/fonts/type1/public/gfscomplutum/
%{_texdir}/texmf-dist/fonts/vf/public/gfscomplutum/
%{_texdir}/texmf-dist/tex/latex/gfscomplutum/

%files -n texlive-gfscomplutum-doc
%{_texdir}/texmf-dist/doc/fonts/gfscomplutum/

%files -n texlive-gfsdidot
%{_datadir}/fonts/gfsdidot
%{_texdir}/texmf-dist/fonts/afm/public/gfsdidot/
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsdidot/
%{_texdir}/texmf-dist/fonts/map/dvips/gfsdidot/
%{_texdir}/texmf-dist/fonts/opentype/public/gfsdidot/
%{_texdir}/texmf-dist/fonts/tfm/public/gfsdidot/
%{_texdir}/texmf-dist/fonts/type1/public/gfsdidot/
%{_texdir}/texmf-dist/fonts/vf/public/gfsdidot/
%{_texdir}/texmf-dist/tex/latex/gfsdidot/

%files -n texlive-gfsdidot-doc
%{_texdir}/texmf-dist/doc/fonts/gfsdidot/

%files -n texlive-gfsneohellenic
%{_datadir}/fonts/gfsneohellenic
%{_texdir}/texmf-dist/fonts/afm/public/gfsneohellenic/
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsneohellenic/
%{_texdir}/texmf-dist/fonts/map/dvips/gfsneohellenic/
%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenic/
%{_texdir}/texmf-dist/fonts/tfm/public/gfsneohellenic/
%{_texdir}/texmf-dist/fonts/type1/public/gfsneohellenic/
%{_texdir}/texmf-dist/fonts/vf/public/gfsneohellenic/
%{_texdir}/texmf-dist/tex/latex/gfsneohellenic/

%files -n texlive-gfsneohellenic-doc
%{_texdir}/texmf-dist/doc/fonts/gfsneohellenic/

%files -n texlive-gfssolomos
%{_datadir}/fonts/gfssolomos
%{_texdir}/texmf-dist/fonts/afm/public/gfssolomos/
%{_texdir}/texmf-dist/fonts/enc/dvips/gfssolomos/
%{_texdir}/texmf-dist/fonts/map/dvips/gfssolomos/
%{_texdir}/texmf-dist/fonts/opentype/public/gfssolomos/
%{_texdir}/texmf-dist/fonts/tfm/public/gfssolomos/
%{_texdir}/texmf-dist/fonts/type1/public/gfssolomos/
%{_texdir}/texmf-dist/fonts/vf/public/gfssolomos/
%{_texdir}/texmf-dist/tex/latex/gfssolomos/

%files -n texlive-gfssolomos-doc
%{_texdir}/texmf-dist/doc/fonts/gfssolomos/

%files -n texlive-gillcm
%{_texdir}/texmf-dist/fonts/map/dvips/gillcm/
%{_texdir}/texmf-dist/fonts/tfm/public/gillcm/
%{_texdir}/texmf-dist/fonts/vf/public/gillcm/
%{_texdir}/texmf-dist/tex/latex/gillcm/

%files -n texlive-gillcm-doc
%{_texdir}/texmf-dist/doc/latex/gillcm/

%files -n texlive-gillius
%license gpl2.txt
%{_datadir}/fonts/gillius
%{_texdir}/texmf-dist/fonts/enc/dvips/gillius/
%{_texdir}/texmf-dist/fonts/map/dvips/gillius/
%{_texdir}/texmf-dist/fonts/opentype/arkandis/gillius/
%{_texdir}/texmf-dist/fonts/tfm/arkandis/gillius/
%{_texdir}/texmf-dist/fonts/type1/arkandis/gillius/
%{_texdir}/texmf-dist/fonts/vf/arkandis/gillius/
%{_texdir}/texmf-dist/tex/latex/gillius/

%files -n texlive-gillius-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/gillius/

%files -n texlive-gnu-freefont
%license gpl3.txt
%{_datadir}/fonts/gnu-freefont
%{_texdir}/texmf-dist/fonts/opentype/public/gnu-freefont/
%{_texdir}/texmf-dist/fonts/truetype/public/gnu-freefont/

%files -n texlive-gnu-freefont-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/fonts/gnu-freefont/

%files -n texlive-gothic
%license collection.txt
%{_texdir}/texmf-dist/fonts/source/public/gothic/
%{_texdir}/texmf-dist/fonts/tfm/public/gothic/

%files -n texlive-gothic-doc
%license collection.txt
%{_texdir}/texmf-dist/doc/fonts/gothic/

%files -n texlive-greenpoint
%license gpl.txt
%{_texdir}/texmf-dist/fonts/source/public/greenpoint/
%{_texdir}/texmf-dist/fonts/tfm/public/greenpoint/

%files -n texlive-greenpoint-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/greenpoint/

%files -n texlive-grotesq
%license gpl.txt
%{_texdir}/texmf-dist/fonts/afm/urw/grotesq/
%{_texdir}/texmf-dist/fonts/map/dvips/grotesq/
%{_texdir}/texmf-dist/fonts/tfm/urw/grotesq/
%{_texdir}/texmf-dist/fonts/type1/urw/grotesq/
%{_texdir}/texmf-dist/fonts/vf/urw/grotesq/
%{_texdir}/texmf-dist/tex/latex/grotesq/

%files -n texlive-grotesq-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/fonts/grotesq/

%files -n texlive-gamebook
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gamebook/

%files -n texlive-gamebook-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gamebook/

%files -n texlive-go
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/go/
%{_texdir}/texmf-dist/fonts/tfm/public/go/
%{_texdir}/texmf-dist/tex/latex/go/

%files -n texlive-go-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/go/

%files -n texlive-gates
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/gates/

%files -n texlive-gates-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/gates/

%files -n texlive-genmisc
%{_texdir}/texmf-dist/tex/generic/genmisc/

%files -n texlive-gb4e
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/gb4e/

%files -n texlive-gb4e-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/gb4e/

%files -n texlive-gmverse
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gmverse/

%files -n texlive-gmverse-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gmverse/

%files -n texlive-ghab
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/ghab/
%{_texdir}/texmf-dist/tex/latex/ghab/

%files -n texlive-ghab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ghab/

%files -n texlive-gost
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/gost/
%{_texdir}/texmf-dist/bibtex/csf/gost

%files -n texlive-gost-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/gost/

%files -n texlive-gentle-doc
%{_texdir}/texmf-dist/doc/plain/gentle/

%files -n texlive-guide-to-latex-doc
%{_texdir}/texmf-dist/doc/latex/guide-to-latex/

%files -n texlive-geometry-de-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/geometry-de/

%files -n texlive-german
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/german/

%files -n texlive-german-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/german/

%files -n texlive-germbib
%{_texdir}/texmf-dist/bibtex/bst/germbib/
%{_texdir}/texmf-dist/tex/latex/germbib/

%files -n texlive-germbib-doc
%{_texdir}/texmf-dist/doc/bibtex/germbib/

%files -n texlive-germkorr
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/germkorr/

%files -n texlive-germkorr-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/germkorr/

%files -n texlive-gfsbaskerville
%{_datadir}/fonts/gfsbaskerville
%{_texdir}/texmf-dist/fonts/afm/public/gfsbaskerville/
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsbaskerville/
%{_texdir}/texmf-dist/fonts/map/dvips/gfsbaskerville/
%{_texdir}/texmf-dist/fonts/opentype/public/gfsbaskerville/
%{_texdir}/texmf-dist/fonts/tfm/public/gfsbaskerville/
%{_texdir}/texmf-dist/fonts/type1/public/gfsbaskerville/
%{_texdir}/texmf-dist/fonts/vf/public/gfsbaskerville/
%{_texdir}/texmf-dist/tex/latex/gfsbaskerville/

%files -n texlive-gfsbaskerville-doc
%{_texdir}/texmf-dist/doc/fonts/gfsbaskerville/

%files -n texlive-gfsporson
%{_datadir}/fonts/gfsporson
%{_texdir}/texmf-dist/fonts/afm/public/gfsporson/
%{_texdir}/texmf-dist/fonts/enc/dvips/gfsporson/
%{_texdir}/texmf-dist/fonts/map/dvips/gfsporson/
%{_texdir}/texmf-dist/fonts/opentype/public/gfsporson/
%{_texdir}/texmf-dist/fonts/tfm/public/gfsporson/
%{_texdir}/texmf-dist/fonts/type1/public/gfsporson/
%{_texdir}/texmf-dist/fonts/vf/public/gfsporson/
%{_texdir}/texmf-dist/tex/latex/gfsporson/

%files -n texlive-gfsporson-doc
%{_texdir}/texmf-dist/doc/fonts/gfsporson/

%files -n texlive-greek-fontenc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/greek-fontenc/

%files -n texlive-greek-fontenc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/greek-fontenc/

%files -n texlive-greek-inputenc
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/greek-inputenc/

%files -n texlive-greek-inputenc-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/greek-inputenc/

%files -n texlive-greekdates
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/greekdates/

%files -n texlive-greekdates-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/greekdates/

%files -n texlive-greektex
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/greektex/

%files -n texlive-greektex-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/greektex/

%files -n texlive-gustlib
%{_texdir}/texmf-dist/bibtex/bib/gustlib/
%{_texdir}/texmf-dist/bibtex/bst/gustlib/
%{_texdir}/texmf-dist/tex/plain/gustlib/

%files -n texlive-gustlib-doc
%{_texdir}/texmf-dist/doc/plain/gustlib/

%files -n texlive-gustprog-doc
%{_texdir}/texmf-dist/doc/support/gustprog/

%files -n texlive-genealogytree
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/genealogytree/

%files -n texlive-genealogytree-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/genealogytree/

%files -n texlive-gincltex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gincltex/

%files -n texlive-gincltex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gincltex/

%files -n texlive-gnuplottex
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/gnuplottex/

%files -n texlive-gnuplottex-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/gnuplottex/

%files -n texlive-gradientframe
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gradientframe/

%files -n texlive-gradientframe-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gradientframe/

%files -n texlive-grafcet
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/grafcet/

%files -n texlive-grafcet-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/grafcet/

%files -n texlive-graphviz
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/graphviz/

%files -n texlive-graphviz-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/graphviz/

%files -n texlive-g-brief
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/g-brief/

%files -n texlive-g-brief-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/g-brief/

%files -n texlive-gauss
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gauss/

%files -n texlive-gauss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gauss/

%files -n texlive-gcard
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gcard/

%files -n texlive-gcard-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gcard/

%files -n texlive-gcite
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gcite/

%files -n texlive-gcite-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gcite/

%files -n texlive-gender
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gender/

%files -n texlive-gender-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gender/

%files -n texlive-genmpage
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/genmpage/

%files -n texlive-genmpage-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/genmpage/

%files -n texlive-getfiledate
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/getfiledate/

%files -n texlive-getfiledate-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/getfiledate/

%files -n texlive-ginpenc
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ginpenc/

%files -n texlive-ginpenc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ginpenc/

%files -n texlive-gitinfo
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gitinfo/

%files -n texlive-gitinfo-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gitinfo/

%files -n texlive-gitinfo2
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gitinfo2/

%files -n texlive-gitinfo2-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gitinfo2/

%files -n texlive-gloss
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/gloss/
%{_texdir}/texmf-dist/bibtex/bst/gloss/
%{_texdir}/texmf-dist/tex/latex/gloss/

%files -n texlive-gloss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gloss/

%files -n texlive-glossaries-danish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-danish/

%files -n texlive-glossaries-danish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-danish/

%files -n texlive-glossaries-dutch
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-dutch/

%files -n texlive-glossaries-dutch-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-dutch/

%files -n texlive-glossaries-english
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-english/

%files -n texlive-glossaries-english-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-english/
%files -n texlive-glossaries-french
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-french/

%files -n texlive-glossaries-french-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-french/
%files -n texlive-glossaries-german
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-german/

%files -n texlive-glossaries-german-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-german/

%files -n texlive-glossaries-irish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-irish/

%files -n texlive-glossaries-irish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-irish/

%files -n texlive-glossaries-italian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-italian/

%files -n texlive-glossaries-italian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-italian/

%files -n texlive-glossaries-magyar
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-magyar/

%files -n texlive-glossaries-magyar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-magyar/

%files -n texlive-glossaries-polish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-polish/

%files -n texlive-glossaries-polish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-polish/

%files -n texlive-glossaries-portuges
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-portuges/

%files -n texlive-glossaries-portuges-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-portuges/

%files -n texlive-glossaries-serbian
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-serbian/

%files -n texlive-glossaries-serbian-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-serbian/

%files -n texlive-glossaries-spanish
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-spanish/

%files -n texlive-glossaries-spanish-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-spanish/

%files -n texlive-gmdoc
%license lppl1.txt
%{_texdir}/texmf-dist/makeindex/gmdoc/
%{_texdir}/texmf-dist/tex/latex/gmdoc/

%files -n texlive-gmdoc-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gmdoc/

%files -n texlive-gmdoc-enhance
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gmdoc-enhance/

%files -n texlive-gmdoc-enhance-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gmdoc-enhance/

%files -n texlive-gmiflink
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gmiflink/

%files -n texlive-gmiflink-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gmiflink/

%files -n texlive-gmutils
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gmutils/

%files -n texlive-gmutils-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gmutils/

%files -n texlive-gmverb
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gmverb/

%files -n texlive-gmverb-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gmverb/

%files -n texlive-graphbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/graphbox/

%files -n texlive-graphbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/graphbox/

%files -n texlive-graphicx-psmin
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/graphicx-psmin/

%files -n texlive-graphicx-psmin-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/graphicx-psmin/

%files -n texlive-graphicxbox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/graphicxbox/

%files -n texlive-graphicxbox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/graphicxbox/

%files -n texlive-grfpaste
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/grfpaste/

%files -n texlive-grfpaste-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/grfpaste/

%files -n texlive-grid
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/grid/

%files -n texlive-grid-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/grid/

%files -n texlive-grid-system
%license apache2.txt
%{_texdir}/texmf-dist/tex/latex/grid-system/

%files -n texlive-grid-system-doc
%license apache2.txt
%{_texdir}/texmf-dist/doc/latex/grid-system/

%files -n texlive-gridset
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gridset/

%files -n texlive-gridset-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gridset/

%files -n texlive-gtl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/gtl/

%files -n texlive-gtl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/gtl/

%files -n texlive-guitlogo
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/guitlogo/

%files -n texlive-guitlogo-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/guitlogo/

%files -n texlive-grundgesetze
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/grundgesetze/

%files -n texlive-grundgesetze-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/latex/grundgesetze/

%files -n texlive-garrigues
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/garrigues/

%files -n texlive-garrigues-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/garrigues/

%files -n texlive-gmp
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gmp/

%files -n texlive-gmp-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gmp/

%files -n texlive-gchords
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/gchords/

%files -n texlive-gchords-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/gchords/

%files -n texlive-gtrcrd
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gtrcrd/

%files -n texlive-gtrcrd-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gtrcrd/

%files -n texlive-guitar
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/guitar/

%files -n texlive-guitar-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/guitar/

%files -n texlive-guitarchordschemes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/guitarchordschemes/

%files -n texlive-guitarchordschemes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/guitarchordschemes/

%files -n texlive-getoptk
%{_texdir}/texmf-dist/tex/plain/getoptk/

%files -n texlive-getoptk-doc
%{_texdir}/texmf-dist/doc/plain/getoptk/

%files -n texlive-gfnotation
%license gpl3.txt
%{_texdir}/texmf-dist/tex/plain/gfnotation/

%files -n texlive-gfnotation-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/plain/gfnotation/

%files -n texlive-graphics-pln
%license lppl1.txt
%{_texdir}/texmf-dist/tex/plain/graphics-pln/

%files -n texlive-graphics-pln-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/plain/graphics-pln/

%files -n texlive-gaceta
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gaceta/

%files -n texlive-gaceta-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gaceta/

%files -n texlive-gatech-thesis
%license gpl.txt
%{_texdir}/texmf-dist/bibtex/bst/gatech-thesis/
%{_texdir}/texmf-dist/makeindex/gatech-thesis/
%{_texdir}/texmf-dist/tex/latex/gatech-thesis/

%files -n texlive-gatech-thesis-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/gatech-thesis/

%files -n texlive-gsemthesis
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gsemthesis/

%files -n texlive-gsemthesis-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gsemthesis/

%files -n texlive-gzt
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gzt/

%files -n texlive-gzt-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gzt/

%files -n texlive-galois
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/galois/

%files -n texlive-galois-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/galois/

%files -n texlive-gastex
%license lppl1.txt
%{_texdir}/texmf-dist/dvips/gastex/
%{_texdir}/texmf-dist/tex/latex/gastex/

%files -n texlive-gastex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gastex/

%files -n texlive-gene-logic
%{_texdir}/texmf-dist/tex/latex/gene-logic/

%files -n texlive-gene-logic-doc
%{_texdir}/texmf-dist/doc/latex/gene-logic/

%files -n texlive-ghsystem
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ghsystem/

%files -n texlive-ghsystem-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ghsystem/

%files -n texlive-gu
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/gu/

%files -n texlive-gu-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/gu/

%files -n texlive-getitems-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/getitems/

%files -n texlive-getitems
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/getitems/

%files -n texlive-gitlog-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gitlog/

%files -n texlive-gitlog
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gitlog/

%files -n texlive-glossaries-extra-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/glossaries-extra/

%files -n texlive-glossaries-extra
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-extra/
%{_texdir}/texmf-dist/bibtex/bib/glossaries-extra/

%files -n texlive-gloss-occitan-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gloss-occitan/

%files -n texlive-gloss-occitan
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gloss-occitan/

%files -n texlive-gobble-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/gobble/

%files -n texlive-gobble
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/gobble/

%files -n texlive-gradstudentresume-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/gradstudentresume/

%files -n texlive-gradstudentresume
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/gradstudentresume/

%files -n texlive-graphics-cfg-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/graphics-cfg/

%files -n texlive-graphics-cfg
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/graphics-cfg/

%files -n texlive-greektonoi-doc
%license gpl3.txt
%{_texdir}/texmf-dist/doc/latex/greektonoi/

%files -n texlive-greektonoi
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/greektonoi/
%{_texdir}/texmf-dist/fonts/map/dvips/greektonoi/

%files -n texlive-graphics-def
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/graphics-def/

%files -n texlive-gitfile-info
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/support/gitfile-info/
%{_texdir}/texmf-dist/tex/latex/gitfile-info/

%files -n texlive-gofonts
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/fonts/gofonts/
%{_texdir}/texmf-dist/fonts/enc/dvips/gofonts/
%{_texdir}/texmf-dist/fonts/map/dvips/gofonts/
%{_texdir}/texmf-dist/fonts/tfm/bh/gofonts/
%{_texdir}/texmf-dist/fonts/truetype/bh/gofonts/
%{_texdir}/texmf-dist/fonts/type1/bh/gofonts/
%{_texdir}/texmf-dist/fonts/vf/bh/gofonts/
%{_texdir}/texmf-dist/tex/latex/gofonts/

%files -n texlive-grant
%doc %{_texdir}/texmf-dist/doc/latex/grant/
%{_texdir}/texmf-dist/tex/latex/grant/

%files -n texlive-grayhints
%license lppl1.2.txt
%doc %{_texdir}/texmf-dist/doc/latex/grayhints/
%{_texdir}/texmf-dist/tex/latex/grayhints/

%files -n texlive-gtrlib-largetrees
%license lppl1.2.txt
%doc %{_texdir}/texmf-dist/doc/latex/gtrlib-largetrees/
%{_texdir}/texmf-dist/tex/latex/gtrlib-largetrees/

%files -n texlive-gatherenum
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/gatherenum/
%doc %{_texdir}/texmf-dist/doc/latex/gatherenum/

%files -n texlive-gbt7714
%license lppl.txt
%{_texdir}/texmf-dist/bibtex/bst/gbt7714/
%{_texdir}/texmf-dist/tex/latex/gbt7714/
%doc %{_texdir}/texmf-dist/doc/bibtex/gbt7714/

%files -n texlive-gentombow
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/gentombow/
%doc %{_texdir}/texmf-dist/doc/latex/gentombow/

%files -n texlive-gfsneohellenicmath
%license ofl.txt
%{_texdir}/texmf-dist/fonts/opentype/public/gfsneohellenicmath/
%{_texdir}/texmf-dist/tex/latex/gfsneohellenicmath/
%doc %{_texdir}/texmf-dist/doc/fonts/gfsneohellenicmath/

%files -n texlive-glossaries-finnish
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/glossaries-finnish/
%doc %{_texdir}/texmf-dist/doc/latex/glossaries-finnish/

%files -n texlive-gotoh
%{_texdir}/texmf-dist/tex/latex/gotoh/
%doc %{_texdir}/texmf-dist/doc/latex/gotoh/

%files -n texlive-graph35
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/graph35/
%doc %{_texdir}/texmf-dist/doc/latex/graph35/

%files -n texlive-graphicxpsd
%{_texdir}/texmf-dist/tex/latex/graphicxpsd/
%doc %{_texdir}/texmf-dist/doc/latex/graphicxpsd/

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
