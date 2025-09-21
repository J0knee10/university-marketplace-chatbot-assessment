# Marketplace Insights for UniMarket Assistant

## 1. Purpose
This document captures research, observations, and trends about university marketplaces and peer-to-peer student resale apps.  
It informs the design and improvement of the **UniMarket Assistant**, ensuring it:
- Resolves common student pain points.  
- Encourages safe and transparent transactions.  
- Adapts to seasonal patterns and evolving campus needs.  

---

## 2. Target Audience
- **Students** (undergrad & postgrad) buying, selling, or trading items.  
- **Faculty & staff** managing surplus items.  
- **Clubs & societies** organizing events or distributing equipment.

Key traits:  
- Limited budgets → seek affordable items.  
- Mobile-first → prefer fast, chat-based guidance.  
- Expect trustworthy info about campus policies and safety.

---

## 3. Pain Points & Opportunities

| Area | Pain Point | Opportunity for Assistant |
|------|------------|---------------------------|
| **Listing items** | New users unsure how to post or edit listings. | Step-by-step guidance (photos, price, category). |
| **Search & discovery** | Difficulty finding relevant items. | Teach filters, categories, and saved searches. |
| **Payments** | Confusion about approved channels; risk of scams. | Provide verified payment methods and scam warnings. |
| **Meet-ups & delivery** | Safety concerns meeting strangers. | Suggest campus-safe meeting spots, daylight, friend accompaniment. |
| **Policy compliance** | Unaware of prohibited items (alcohol, drugs, weapons). | Explain rules, suggest alternatives, escalate violations. |
| **Fraud & abuse** | Fake accounts, phishing, harassment. | Report scams, block offenders, escalate threats. |
| **Technical issues** | Upload failures, app crashes. | Troubleshooting steps and guidance to tech support. |
| **Multi-topic queries** | Users combine unrelated questions. | Detect and ask which issue to address first. |

---

## 4. Safety & Trust Considerations
- Emphasize campus-specific safety: on-campus meetups, public spots.  
- Never request sensitive info (bank details, OTPs).  
- Escalate threats, harassment, or scams promptly.  
- Integrate with university verification systems (e.g., `.edu` email sign-in, student ID confirmation) to reduce fake accounts.

---

## 5. Seasonal Patterns
- **Semester start**: High textbook demand, furniture for dorms, clothes for lessons  
- **Move-in / move-out periods**: Furniture, appliances, and leftover supplies.  
- **Exam season**: Stationery, study aids, tutoring requests.  
- **Graduation**: Clearance sales for furniture, electronics, and study materials.  

> Assistant can provide **timely tips** or **highlight relevant categories** based on season.

---

## 6. Integration Needs
- University email verification for trust and account validation.  
- Optional: link to campus events calendar to suggest safe meetup locations.  
- Authentication for clubs or societies posting bulk items.  

---

## 7. Industry Benchmarks
- **Facebook Marketplace** – easy listing; lacks campus-specific safety guidance.  
- **Carousell** – strong chat support; highlights ratings but less proactive about scams.  
- **Student-only resale platforms** – small scale, high trust via `.edu` verification.  

**Insight:** Students prefer platforms that blend **ease of use + strong safety and trust mechanisms**.

---

## 8. Future Opportunities
| Theme | Idea |
|-------|------|
| Smart recommendations | Suggest price ranges or popular categories. |
| Automated dispute wizard | Step-by-step guidance for reporting issues. |
| Accessibility | Screen reader optimization, multilingual support. |
| Analytics | Track queries triggering escalations or confusion. |
| Proactive safety tips | Quick reminders triggered by keywords (“meet”, “cash”). |

---

## 9. How Insights Guide Prompt Design
- Map insights to instructions or escalation rules in `prompt.md`.  
- Golden tests (`test-cases.json`) validate coverage (scams, safety, payment guidance).  
- Updates should cite which insight or seasonal trend they address.  

---

## 10. References
- Student survey on campus resale habits (2025).  
- University risk management office safety guidelines.  
- [Facebook Marketplace Community Standards](https://www.facebook.com/help/marketplace/)  
- [Carousell Safety Tips](https://support.carousell.com/)  
