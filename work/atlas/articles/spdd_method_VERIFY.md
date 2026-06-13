# spdd_method_VERIFY

Статус: `verification_recipe_final`.

Запускать из корня пакета `/mnt/data/spdd_work` или из соответствующего корня репозитория после распаковки.

```bash
python3 - <<'PY'
from pathlib import Path
import re
article = Path('work/atlas/articles/spdd_method.md')
text = article.read_text(encoding='utf-8')
required = [
  'work/atlas/articles/spdd_method.md',
  'work/atlas/articles/spdd_method_source_usage.md',
  'work/atlas/articles/spdd_method_source_transfer_ledger.md',
  'work/atlas/articles/spdd_method_image_plan.md',
  'work/atlas/articles/spdd_method_external_image_queue.md',
  'work/atlas/articles/spdd_method_open_questions.md',
  'work/atlas/articles/spdd_method_theory_links.md',
  'work/atlas/articles/spdd_method_degradation_and_duplication_audit.md',
  'work/atlas/articles/spdd_method_readiness_report.md',
]
for f in required:
    p = Path(f)
    assert p.exists() and p.stat().st_size > 0, f'missing/empty: {f}'
assert text.count('<img ') == 8, 'expected 8 local images'
assert text.count('data-asset-status="external-real-candidate"') == 3, 'expected 3 external placeholders'
assert '## Внешние изображения для asset-pass' in text, 'missing asset-pass section'
for src in re.findall(r'<img src="([^"]+)"', text):
    assert (article.parent / src).resolve().exists(), f'missing image path: {src}'
for label, url in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', text):
    if not url.startswith(('http://','https://','#','mailto:')) and not url.startswith('../../../content/assets'):
        assert (article.parent / url).resolve().exists(), f'missing local link: {url}'
for i, line in enumerate(text.splitlines(), 1):
    assert len(line) <= 900, f'line too long: {i}'
for bad in ['отрицательное пространство','лёгкий отпечаток','инструментальная поверхность','петля сопровождения','поломка инструментальной поверхности']:
    assert bad not in text, f'style regression: {bad}'
print('spdd_method verification OK')
PY
```

Ожидаемый результат: `spdd_method verification OK`.

Дополнительная человеческая проверка перед публикацией:

- открыть три external-real placeholders и решить, скачивать/локализовать ли кандидаты;
- проверить актуальность OpenSPDD README/templates;
- проверить внешние ссылки;
- убрать или заменить нижний временный asset-pass раздел после локализации изображений.
