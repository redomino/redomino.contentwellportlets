#!/usr/bin/env bash
cd $(dirname $0)
rm ./rebuild_i18n.log

i18ndude rebuild-pot --pot ./contentwellportlets.pot --merge ./contentwellportlets-manual.pot --create redomino.contentwellportlets ../ ../profiles ../browser || exit 1
i18ndude sync        --pot ./contentwellportlets.pot ./*/LC_MESSAGES/contentwellportlets.po

i18ndude rebuild-pot --pot ../i18n/contentwellportlets.pot --merge ../i18n/contentwellportlets-manual.pot --create plone ../ ../profiles ../browser || exit 1
i18ndude sync        --pot ../i18n/contentwellportlets.pot ../i18n/contentwellportlets-*.po

WARNINGS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-WARN' | wc -l`
ERRORS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-ERROR' | wc -l`
FATAL=`find . -name "*pt"  | xargs i18ndude find-untranslated | grep -e '^-FATAL' | wc -l`

echo
echo There are $ERRORS errors \(almost definitely missing i18n markup\)
echo There are $WARNINGS warnings \(possibly missing i18n markup\)
echo There are $FATAL fatal errors \(template could not be parsed, eg. if it\'s not html\)
echo For more details, run \'find . -name \"\*pt\" \| xargs i18ndude find-untranslated\' or 
echo Look the rebuild i18n log generate for this script called \'rebuild_i18n.log\' on locales dir 

touch ./rebuild_i18n.log

find . -name "*pt" | xargs i18ndude find-untranslated > rebuild_i18n.log


