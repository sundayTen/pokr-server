const fs = require('fs');
const results = JSON.parse(
  fs.readFileSync('./pokr-web/lhci_reports/manifest.json'),
);

let comments = '';

const formatResult = (res) => Math.round(res * 100);
const score = (res) => (res >= 90 ? '🟢' : res >= 50 ? '🟠' : '🔴');

results.forEach((result) => {
  const { summary, jsonPath } = result;
  const details = JSON.parse(fs.readFileSync(jsonPath));
  const { audits } = details;

  Object.keys(summary).forEach(
    (key) => (summary[key] = formatResult(summary[key])),
  );

  const comment = [
    `⚡️ Lighthouse report!`,
    `| Category | Score |`,
    `| --- | --- |`,
    `| ${score(summary.performance)} Performance | ${summary.performance} |`,
  ].join('\n');

  const detail = [
    `| Category | Score |`,
    `| --- | --- |`,
    `| ${score(
      audits['first-contentful-paint'].score * 100,
    )} First Contentful Paint | ${
      audits['first-contentful-paint'].displayValue
    } |`,
  ].join('\n');
  comments += comment + '\n' + detail + '\n';
});

core.setOutput('comments', comments);
