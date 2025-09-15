

===== SCORECARD_DEFINITION.MD =====

# 🧠 CRO Scorecard Definition

This scorecard is used to evaluate A/B test hypotheses before launch.
Each dimension is scored on a scale of 1–5, with higher scores representing more desirable attributes.

---

## Score Dimensions

### 1. Impact
*How significantly could this test move the primary goal or KPI if it succeeds?*

- 5 – High-leverage test on a key decision point
- 3 – Moderate impact
- 1 – Minor or superficial

### 2. Confidence
*How confident are we that this change will drive improvement, based on data, precedent, or user feedback?*

- 5 – Strong supporting data or past performance
- 3 – Directionally informed
- 1 – Speculative or gut feel

### 3. Effort
*How much development/design work is required to implement and QA this test?*

(Lower effort = higher score)

- 5 – Simple visual/copy
- 3 – Some engineering required
- 1 – Complex feature or backend work

### 4. Clarity & User Trust
*Does this help users make informed decisions without confusion or manipulation?*

- 5 – Improves clarity, transparency
- 3 – Neutral
- 1 – Risk of misleading/frustrating users

---

## Total Score
Sum of all four dimensions (Max = 20).


===== TESTS =====



--- FILE: 2025-01-09-shared-hosting-price-ladder.md ---

# 🧪 Experiment Title
Shared Hosting Price Ladder with HP595 Coupon

## 🎯 Hypothesis & Goals

**Hypothesis**
If we create a clear price ladder effect on the Shared Hosting product page using the HP595 coupon to reduce the Growth plan price, then users will more easily see value differentiation between plans and increase conversions, because clear pricing hierarchy helps customers choose the right plan.

**Primary Goal**
Signup

**Secondary Goal**
Revenue

**Other Secondary Goals**
- Signup: Essentials
- Signup: Growth  
- Signup: Premium
- Signup: Elite

---

## 📍 Context

- **Page**: Shared Hosting Product Page
- **Device**: Mobile and Desktop
- **Traffic Volume**: High
- **User Insight / Pain Point**: Users struggle with value differentiation between hosting plans without clear price progression

---

## 🛠️ Test Variations

- **Control**: Current Shared Hosting pricing display
- **Variant A**: Price ladder with HP595 coupon applied to Growth plan for clear value progression

---

## 🧠 AI Scorecard (Pre-Test Evaluation)

| Criteria               | Score (1–5) | Rationale |
|------------------------|-------------|-----------|
| Impact                 | 4           | High-traffic product page, core monetization point |
| Confidence             | 4           | Price ladder psychology well-documented in conversion optimization |
| Effort                 | 4           | Requires coupon system integration and pricing display updates |
| Clarity & User Trust   | 5           | Improves pricing transparency and decision clarity |
| **Total**              | **17**      |           |

---

## 📈 Test Results
(To be filled post-test)

---

## 🧾 Reflection & Insights
(To be filled post-test)

---

## 📎 Attachments
- Screenshots of current pricing display
- HP595 coupon configuration details
- VWO Test ID: TBD

--- FILE: 2025-08-01-plan-layout-redesign.md ---

# 🧪 Experiment Title
Redesign Pricing Plan Layout to Improve Plan Selection Clarity

## 🎯 Hypothesis & Goals

**Hypothesis**
If we redesign the pricing plan layout to better differentiate plans visually, then users will more easily choose the right plan, because the current structure lacks hierarchy and overwhelms users.

**Primary Goal**
Increase mid-tier or paid plan selection

**Secondary Goal**
Reduce plan compare clicks, increase clarity engagement

---

## 📍 Context

- **Page**: WordPress Hosting Pricing Page
- **Device**: Desktop
- **Traffic Volume**: High
- **User Insight / Pain Point**: Users hesitate or bounce at pricing due to dense, undifferentiated layout

---

## 🛠️ Test Variations

- **Control**: Flat 4-column layout, dense feature bullets
- **Variant A**: Ladder-style visual hierarchy with color emphasis
- **Variant B**: Simplified bullets + “Best for…” persona tags

---

## 🧠 AI Scorecard (Pre-Test Evaluation)

| Criteria               | Score (1–5) | Rationale |
|------------------------|-------------|-----------|
| Impact                 | 5           | High-traffic, high-stakes decision point |
| Confidence             | 3           | Supported by UX principles but lacks direct test precedent |
| Effort                 | 2           | Design + responsive layout work |
| Clarity & User Trust   | 5           | Enhances decision clarity with no manipulation |
| **Total**              | **15**      |           |

---

## 📈 Test Results
(To be filled post-test)

---

## 🧾 Reflection & Insights
(To be filled post-test)

---

## 📎 Attachments
- Screenshot of current page
- VWO Test ID: TBD


--- FILE: 2025-08-28-domain-order-form-update-v2.md ---

# 🧪 Experiment Title
Domain Order Form Update v3

## 🎯 Hypothesis & Goals

**Hypothesis**
If we implement the refined domain order form layout incorporating learnings from v1 testing, then users will more easily complete their domain orders, because the optimized visual hierarchy and flow improvements address the key usability issues identified in the previous variant.

**Primary Goal**
Increase domain order conversions

**Secondary Goal**
Reduce form abandonment, increase order completion clarity

---

## 📍 Context

- **Page**: Domain Order Form
- **Device**: Mobile and Desktop (100% traffic)
- **Markets**: CA, COM, AU
- **Traffic Volume**: High
- **Test Status**: Live (started 2025-01-15)
- **User Insight / Pain Point**: Users hesitate or abandon the domain order form due to dense, undifferentiated layout

---

## 🛠️ Test Variations

- **Control**: Current domain order form
- **Variant A**: Refined domain order form with optimized flow and visual hierarchy based on v1 learnings

---

## 🧠 AI Scorecard (Pre-Test Evaluation)

| Criteria               | Score (1–5) | Rationale |
|------------------------|-------------|-----------|
| Impact                 | 5           | High-traffic, high-stakes decision point |
| Confidence             | 3           | Supported by UX principles but lacks direct test precedent |
| Effort                 | 2           | Design + responsive layout work |
| Clarity & User Trust   | 5           | Enhances decision clarity with no manipulation |
| **Total**              | **15**      |           |

---

## 📈 Test Results
(To be filled post-test)

---

## 🧾 Reflection & Insights
(To be filled post-test)

---

## 📎 Attachments
- Screenshot of current page
- VWO Test ID: https://app.vwo.com/#/test/ab/339/report?accountId=11990

--- FILE: test_template.md ---

# 🧪 Experiment Title
[Insert Title Here]

## 🎯 Hypothesis & Goals

**Hypothesis**
If we [describe the change], then [expected result], because [reason].

**Primary Goal**
[Main metric to improve]

**Secondary Goal**
[Supporting or diagnostic metric]

---

## 📍 Context

- **Page**: [e.g., Pricing Page]
- **Device**: [e.g., Desktop]
- **Traffic Volume**: [High/Medium/Low]
- **User Insight / Pain Point**: [Observed user behavior or feedback]

---

## 🛠️ Test Variations

- **Control**: [Description]
- **Variant A**: [Description]
- *(Add more as needed)*

---

## 🧠 AI Scorecard (Pre-Test Evaluation)

| Criteria               | Score (1–5) | Rationale |
|------------------------|-------------|-----------|
| Impact                 |             | [Why it matters] |
| Confidence             |             | [Evidence or reasoning] |
| Effort                 |             | [Implementation complexity] |
| Clarity & User Trust   |             | [User benefit, honesty, clarity] |
| **Total**              |             |           |

---

## 📈 Test Results
(To be filled post-test)

---

## 🧾 Reflection & Insights
(To be filled post-test)

---

## 📎 Attachments
[List of links, screenshots, or data export]


===== BRIEFS =====



--- FILE: 2025-01-09-shared-hosting-price-ladder-brief.md ---

# 📘 CRO Test Brief: Shared Hosting Price Ladder

## ✅ Summary
We propose testing a price ladder implementation on the Shared Hosting product page using HP595 coupon to create clear value differentiation across plans and improve conversion rates.

## 🎯 Hypothesis
If we create a clear price ladder effect using the HP595 coupon to reduce the Growth plan price, then users will more easily see value differentiation between plans and increase conversions, because clear pricing hierarchy helps customers choose the right plan.

## 🧪 Variants
- **Control**: Current Shared Hosting pricing display
- **Variant A**: Price ladder with HP595 coupon applied to Growth plan for clear value progression

## 🧠 Pre-Test Scoring

| Criteria               | Score (1–5) | Rationale |
|------------------------|-------------|-----------|
| Impact                 | 4           | High-traffic product page, core monetization point |
| Confidence             | 4           | Price ladder psychology well-documented in conversion optimization |
| Effort                 | 4           | Requires coupon system integration and pricing display updates |
| Clarity & User Trust   | 5           | Improves pricing transparency and decision clarity |
| **Total**              | 17          |           |

## 🎯 Goals
- **Primary Goal**: Signup
- **Secondary Goal**: Revenue
- **Other Secondary Goals**: Signup: Essentials, Signup: Growth, Signup: Premium, Signup: Elite

## ⏱️ Duration
Est. 14–21 days

## 🧰 Tools
VWO, GA, Hotjar

## 📎 Attachments
- Screenshots of current pricing display
- HP595 coupon configuration details
- VWO Test ID: TBD

--- FILE: 2025-08-01-plan-layout-redesign-brief.md ---

# 📘 CRO Test Brief: Plan Layout Redesign

## ✅ Summary
We propose testing a redesigned pricing plan layout to improve plan selection clarity and increase conversions. The current layout overwhelms users and lacks visual hierarchy.

## 🎯 Hypothesis
If we redesign the pricing plan layout to simplify decision-making and visually differentiate plans, then users will convert at higher rates, because the current flat design causes indecision.

## 🧪 Variants
- **Control**: Flat 4-column layout
- **Variant A**: Staggered pricing ladder layout
- **Variant B**: Simplified bullets with persona labels

## 🧠 Pre-Test Scoring

| Criteria               | Score (1–5) | Rationale |
|------------------------|-------------|-----------|
| Impact                 | 5           | Key monetization point |
| Confidence             | 3           | Good rationale, modest prior evidence |
| Effort                 | 2           | Layout and copy changes only |
| Clarity & User Trust   | 5           | Reduces cognitive load |
| **Total**              | 15          |           |

## 🎯 Goals
- **Primary Goal**: Paid plan selection
- **Secondary Goal**: Reduced plan compare friction

## ⏱️ Duration
Est. 14–21 days

## 🧰 Tools
VWO, GA, Hotjar

## 📎 Attachments
- Screenshot of current
- Markdown test log


--- FILE: 2025-08-28-domain-order-form-update-v2-brief.md ---

# 📘 CRO Test Brief: Domain Order Form Update v3

## ✅ Summary
We are testing a refined domain order form layout incorporating learnings from v1 to improve domain selection clarity and increase conversions. Test is live in CA, COM, and AU markets with 100% traffic coverage.

## 🎯 Hypothesis
If we implement the refined domain order form layout incorporating learnings from v1 testing, then users will more easily complete their domain orders, because the optimized visual hierarchy and flow improvements address the key usability issues identified in the previous variant.

## 🧪 Variants
- **Control**: Current domain order form
- **Variant A**: Refined domain order form with optimized flow and visual hierarchy based on v1 learnings

## 🧠 Pre-Test Scoring

| Criteria               | Score (1–5) | Rationale |
|------------------------|-------------|-----------|
| Impact                 | 5           | High-traffic, high-stakes decision point |
| Confidence             | 3           | Supported by UX principles but lacks direct test precedent |
| Effort                 | 2           | Design + responsive layout work |
| Clarity & User Trust   | 5           | Enhances decision clarity with no manipulation |
| **Total**              | 15          |           |

## 🎯 Goals
- **Primary Goal**: Increase domain order conversions
- **Secondary Goal**: Reduce form abandonment, increase order completion clarity

## ⏱️ Duration
Est. 14–21 days (Started: 2025-01-15)

## 🌍 Markets & Coverage
- **Markets**: CA, COM, AU
- **Traffic**: 100% (Mobile and Desktop)

## 🧰 Tools
VWO, GA, Hotjar

## 📎 Attachments
- Screenshot of current page
- VWO Test ID: https://app.vwo.com/#/test/ab/339/report?accountId=11990

--- FILE: test_brief_template.md ---

# 📘 CRO Test Brief Template

## ✅ Summary
[Short description of the test's purpose and what it's trying to improve.]

## 🎯 Hypothesis
If we [make a change], then [expected behavior], because [why it should work].

## 🧪 Variants
- **Control**: [Describe current state]
- **Variant A/B**: [Describe each variation]

## 🧠 Pre-Test Scoring

| Criteria               | Score (1–5) | Rationale |
|------------------------|-------------|-----------|
| Impact                 |             |           |
| Confidence             |             |           |
| Effort                 |             |           |
| Clarity & User Trust   |             |           |
| **Total**              |             |           |

## 🎯 Goals
- **Primary Goal**: [Conversion action]
- **Secondary Goal**: [Engagement/UX proxy]

## ⏱️ Duration
Est. [X days] to significance

## 🧰 Tools
[VWO, GA, Hotjar, etc.]

## 📎 Attachments
[List of files, screenshots, links]
