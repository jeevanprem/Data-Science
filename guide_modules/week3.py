# -*- coding: utf-8 -*-
"""Week 3 Module: Probability, Random Variables & Hypothesis Testing"""

def get_week3_content():
    return """
        <!-- ============================================================ -->
        <!-- WEEK 3 MODULE -->
        <!-- ============================================================ -->
        <article class="week-module" id="week3">
            <header class="module-header">
                <div class="module-title-group">
                    <h2><span class="module-pill">Week 03</span> Probability, Random Variables &amp; Hypothesis Testing</h2>
                    <div class="module-lectures">NPTEL Lectures 19–22 | Probability Spaces, Discrete &amp; Continuous Distributions, Expectation, CLT, and Hypothesis Testing</div>
                </div>
            </header>

            <div class="module-body">
                <!-- Section 1: Core Concepts -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 1. Core Concepts &amp; Systematic Breakdown</h3>
                    <p>
                        Data is inherently subject to noise, measurement uncertainty, and random variability. Probability provides the rigorous mathematical calculus to model uncertainty, while statistical inference allows engineers to deduce population characteristics from finite empirical samples.
                    </p>

                    <div style="margin-top: 14px;">
                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">A. Measures of Central Tendency &amp; Data Types</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Mean (Arithmetic Average):</strong> $\\bar{X} = \\frac{1}{n}\\sum x_i$. Appropriate for continuous, symmetrically distributed data without severe outliers. Sensitive to extreme values.</li>
                            <li><strong>Median (50th Percentile):</strong> Middle value of sorted observations. Robust to outliers and extreme skewness (preferred for income, house prices). Appropriate for ordinal and continuous data.</li>
                            <li><strong>Mode (Most Frequent Value):</strong> The single most frequent observation or category.
                                <br>• <strong>CRITICAL NPTEL EXAM RULE:</strong> <em>Mode is the ONLY measure of central tendency that can be computed for categorical / nominal data!</em> (e.g. eye color, car brand, machine brand). You cannot compute the mean or median of categorical labels.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">B. Probability Axioms, Bayes' Theorem &amp; Sampling Schemes</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Multiplication Rule &amp; Conditional Probability:</strong>
                                $$P(A \\cap B) = P(A \\mid B) P(B) = P(B \\mid A) P(A)$$
                                If $A$ and $B$ are independent, $P(A \\cap B) = P(A) P(B)$ and $P(A \\mid B) = P(A)$.
                            </li>
                            <li><strong>Law of Total Probability &amp; Bayes' Rule:</strong> If events $B_1, B_2, \\dots, B_k$ partition the sample space:
                                $$P(A) = \\sum_{j=1}^k P(A \\mid B_j) P(B_j)$$
                                $$P(B_i \\mid A) = \\frac{P(A \\mid B_i) P(B_i)}{\\sum_{j=1}^k P(A \\mid B_j) P(B_j)}$$
                                <em>Classic NPTEL Problem:</em> Factory receives components from Supplier 1 ($60\\%$, $2\\%$ defective) and Supplier 2 ($40\\%$, $5\\%$ defective). If a randomly chosen item is defective, the probability it came from Supplier 1 is:
                                $$P(S_1 \\mid D) = \\frac{0.02 \\times 0.60}{(0.02 \\times 0.60) + (0.05 \\times 0.40)} = \\frac{0.012}{0.012 + 0.020} = \\frac{0.012}{0.032} = 0.375 \\; (37.5\\%)$$
                            </li>
                            <li><strong>Sampling With vs Without Replacement:</strong>
                                <br>• <em>With Replacement:</em> Trials are independent; constant probability of success $\\implies$ <strong>Binomial Distribution</strong> $B(n, p)$.
                                <br>• <em>Without Replacement:</em> Trials are dependent; finite population of size $N$ with $K$ successes $\\implies$ <strong>Hypergeometric Distribution</strong>:
                                $$P(X = k) = \\frac{\\binom{K}{k} \\binom{N - K}{n - k}}{\\binom{N}{n}}$$
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">C. Mathematical Expectation, Variance, and Scaling Rules</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Expected Value $E[X]$:</strong> Discrete: $E[X] = \\sum_i x_i P(X = x_i)$. Continuous: $E[X] = \\int_{-\\infty}^{\\infty} x f(x) dx$.
                                <br>Linearity: $E[aX + bY + c] = aE[X] + bE[Y] + c$ (holds universally, even if dependent!).
                            </li>
                            <li><strong>Variance $\\text{Var}(X)$:</strong> Measures dispersion: $\\text{Var}(X) = E[X^2] - (E[X])^2$.
                                <ul style="margin-left: 18px; margin-top: 4px;">
                                    <li>$\\text{Var}(aX + c) = a^2 \\text{Var}(X)$ (constants have zero variance; scalars square!).</li>
                                    <li>Independent variables: $\\text{Var}(aX + bY) = a^2 \\text{Var}(X) + b^2 \\text{Var}(Y)$.</li>
                                    <li>$$\\mathbf{\\text{Var}(aX - bY) = a^2 \\text{Var}(X) + b^2 \\text{Var}(Y)} \\quad \\text{(CRUCIAL: Variances NEVER subtract!)}$$</li>
                                </ul>
                            </li>
                            <li><strong>Covariance &amp; Pearson Correlation:</strong> $\\text{Cov}(X, Y) = E[XY] - \\mu_X \\mu_Y$.
                                <br>Correlation: $\\rho_{XY} = \\frac{\\text{Cov}(X, Y)}{\\sigma_X \\sigma_Y} \\in [-1, 1]$. Standardized, dimensionless, scale-invariant.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">D. Sample Statistics &amp; Sampling Distributions</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Sample Mean:</strong> $\\bar{X} = \\frac{1}{n}\\sum X_i$, $E[\\bar{X}] = \\mu$, $\\text{SE}(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}}$.</li>
                            <li><strong>Central Limit Theorem (CLT):</strong> For iid samples with mean $\\mu$ and finite $\\sigma^2$, as $n \\ge 30$, $\\frac{\\bar{X} - \\mu}{\\sigma / \\sqrt{n}} \\xrightarrow{d} N(0, 1)$, regardless of population shape.</li>
                            <li><strong>Sample Variance ($s^2$):</strong> $s^2 = \\frac{1}{n-1}\\sum (X_i - \\bar{X})^2$. Unbiased because of Bessel's correction ($n-1$).</li>
                            <li><strong>Sampling Distribution of Sample Variance (Chi-Square):</strong>
                                If a random sample $X_1, \\dots, X_n$ is drawn from a normal population $N(\\mu, \\sigma^2)$, the quantity:
                                $$\\frac{(n - 1) s^2}{\\sigma^2} \\sim \\chi^2_{n - 1}$$
                                follows a Chi-Square distribution with $n - 1$ degrees of freedom. Expected value is $E[\\chi^2_{n-1}] = n - 1$, and variance is $2(n - 1)$.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">E. Hypothesis Testing Framework &amp; Decision Rules</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Null ($H_0$) &amp; Alternative ($H_a$):</strong> $H_0: \\mu = \\mu_0$ vs $H_a: \\mu \\ne \\mu_0$ (two-tailed) or $H_a: \\mu &gt; \\mu_0$ (one-tailed).</li>
                            <li><strong>Errors:</strong> Type I Error ($\\alpha$) = Rejecting true $H_0$ (significance level). Type II Error ($\\beta$) = Failing to reject false $H_0$. Power $= 1 - \\beta$.</li>
                            <li><strong>Decision Rule:</strong> $\\text{Reject } H_0 \\iff p\\text{-value} &lt; \\alpha$.</li>
                            <li><strong>One-Sample Z-Test:</strong> (Known $\\sigma$) $Z = \\frac{\\bar{X} - \\mu_0}{\\sigma / \\sqrt{n}} \\sim N(0, 1)$. Reject if $|Z| &gt; 1.96$ for $\\alpha = 0.05$.</li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">F. Two-Sample &amp; Paired $t$-Tests</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Independent Two-Sample $t$-Test:</strong> Compares means of two distinct groups (e.g. Group A vs Group B).
                                $$t = \\frac{\\bar{X}_1 - \\bar{X}_2}{s_p \\sqrt{\\frac{1}{n_1} + \\frac{1}{n_2}}}, \\quad s_p^2 = \\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}, \\quad \\text{df} = n_1 + n_2 - 2$$
                            </li>
                            <li><strong>Paired $t$-Test (Repeated Measures):</strong> Used when observations are matched pairs on the SAME subjects (e.g., patient blood pressure Before vs After treatment).
                                <br>• Computes differences $d_i = X_{\\text{after}, i} - X_{\\text{before}, i}$.
                                <br>• Reduces to a one-sample $t$-test on difference variable $d$:
                                $$t = \\frac{\\bar{d} - 0}{s_d / \\sqrt{n}}, \\quad \\text{df} = n - 1$$
                            </li>
                        </ul>
                    </div>

                    <!-- Callout: Exam Traps -->
                    <div class="callout-card callout-trap">
                        <div class="callout-icon">⚠️</div>
                        <div class="callout-content">
                            <h4>NPTEL Exam Pitfall: Variance of Difference vs Sum</h4>
                            <p>
                                A classic trap in Week 3 assignments: If $X$ and $Y$ are independent, what is $\\text{Var}(4X - 2Y + 5)$?
                                <br>$$\\text{Var}(4X - 2Y + 5) = 4^2 \\text{Var}(X) + (-2)^2 \\text{Var}(Y) + 0 = 16\\text{Var}(X) + 4\\text{Var}(Y)$$
                                <strong>Common Error:</strong> Students write $16\\text{Var}(X) - 4\\text{Var}(Y)$. Variances NEVER subtract! Squaring $(-2)^2$ yields $+4$. Constant $+5$ has zero variance.
                            </p>
                        </div>
                    </div>

                    <!-- Callout: Professor's Solving Strategy -->
                    <div class="callout-card callout-strategy">
                        <div class="callout-icon">🎯</div>
                        <div class="callout-content">
                            <h4>Professor's Z-Test 30-Second Execution Blueprint</h4>
                            <p>
                                1. Identify given values: Sample mean $\\bar{X}$, Null mean $\\mu_0$, Population standard deviation $\\sigma$, Sample size $n$.
                                <br>2. Calculate Standard Error: $\\text{SE} = \\sigma / \\sqrt{n}$.
                                <br>3. Calculate Test Statistic: $Z = (\\bar{X} - \\mu_0) / \\text{SE}$.
                                <br>4. Compare with critical value ($1.96$ for $5\\%$ two-tailed) or compute $p = 2(1 - \\Phi(|Z|))$.
                                <br>5. Conclude: If $|Z| &gt; 1.96$ or $p &lt; 0.05$, reject $H_0$!
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 2: Formatted Formulas & Rules Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 2. Essential Mathematical Formulas &amp; Test Statistics</h3>
                    <div class="formula-grid">
                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Variance of Linear Combination</span>
                                <span class="nav-badge">Probability</span>
                            </div>
                            <div class="formula-math">
                                $$\\text{Var}(aX \\pm bY) = a^2\\text{Var}(X) + b^2\\text{Var}(Y) \\pm 2ab\\text{Cov}(X,Y)$$
                            </div>
                            <div class="formula-desc">For independent variables, $\\text{Cov}(X,Y) = 0$, so $\\text{Var}(aX - bY) = a^2\\text{Var}(X) + b^2\\text{Var}(Y)$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If independent $X, Y$ have $\\text{Var}(X) = 4, \\text{Var}(Y) = 9$, what is $\\text{Var}(3X - 2Y + 7)$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Constants shift location without affecting spread: $\\text{Var}(3X - 2Y + 7) = 3^2(4) + (-2)^2(9) + 0 = 36 + 36 = 72$. (Note: negative coefficient squared becomes $+4$).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If $\\text{Cov}(X, Y) = 2, \\text{Var}(X) = 5, \\text{Var}(Y) = 3$, find $\\text{Var}(2X + Y)$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{Var}(2X + Y) = 2^2(5) + 1^2(3) + 2(2)(1)(2) = 20 + 3 + 8 = 31$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>One-Sample Z-Statistic</span>
                                <span class="nav-badge">Inference</span>
                            </div>
                            <div class="formula-math">
                                $$Z = \\frac{\\bar{X} - \\mu_0}{\\sigma / \\sqrt{n}} \\sim N(0, 1)$$
                            </div>
                            <div class="formula-desc">Standardizes difference between observed sample mean $\\bar{X}$ and hypothesized mean $\\mu_0$ under known population standard deviation $\\sigma$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Given $n = 36, \\bar{X} = 52, \\mu_0 = 50, \\sigma = 6$, calculate $Z$ and state decision at $\\alpha = 0.05$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{SE} = 6/\\sqrt{36} = 1.0$. $Z = (52 - 50)/1.0 = 2.00$. Since $|Z| = 2.00 &gt; 1.96$, reject $H_0$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> How does $Z$ change if sample size is quadrupled ($4n$) for fixed $(\\bar{X} - \\mu_0)$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{SE} \\propto 1/\\sqrt{n}$. Quadrupling $n$ halves the denominator ($1/\\sqrt{4} = 1/2$), which exactly doubles the test statistic $Z$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Sample Variance (Unbiased)</span>
                                <span class="nav-badge">Bessel</span>
                            </div>
                            <div class="formula-math">
                                $$s^2 = \\frac{1}{n-1}\\sum_{i=1}^n (X_i - \\bar{X})^2$$
                            </div>
                            <div class="formula-desc">Divisor $n-1$ accounts for loss of 1 degree of freedom from estimating the population mean via $\\bar{X}$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Compute sample variance $s^2$ for sample $\{2, 4, 6, 8, 10\}$ ($n = 5$).</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\bar{X} = 6$. Squared deviations: $(2-6)^2=16, (4-6)^2=4, 0, 4, 16$ (sum = $40$). Bessel's divisor $n-1 = 4$: $s^2 = 40/4 = 10$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Why does R's <code>var()</code> divide by $n-1$ instead of $n$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Dividing by $n$ produces a biased underestimate ($E[s_n^2] = \\frac{n-1}{n}\\sigma^2$). The $n-1$ divisor ensures an unbiased estimator ($E[s^2] = \\sigma^2$).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Pearson Correlation Coefficient</span>
                                <span class="nav-badge">Association</span>
                            </div>
                            <div class="formula-math">
                                $$\\rho_{XY} = \\frac{\\text{Cov}(X, Y)}{\\sigma_X \\sigma_Y} \\in [-1, 1]$$
                            </div>
                            <div class="formula-desc">Measures linear association strength and direction. Scale-invariant and dimensionless.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> If $\\text{Cov}(X, Y) = 15, s_X = 5, s_Y = 6$, find $r_{XY}$ and the SLR $R^2$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $r_{XY} = 15 / (5 \\times 6) = 0.50$. In simple linear regression, $R^2 = r_{XY}^2 = (0.50)^2 = 0.25$ (25% variance explained).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If $Y = -3X + 7$, what is $\\text{cor}(X, Y)$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Perfect linear inverse relationship with negative slope ($-3 &lt; 0$) yields $\\text{cor}(X, Y) = -1.00$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Bayes' Rule with Total Probability</span>
                                <span class="nav-badge">Inference</span>
                            </div>
                            <div class="formula-math">
                                $$P(B_1 \\mid A) = \\frac{P(A \\mid B_1) P(B_1)}{P(A \\mid B_1) P(B_1) + P(A \\mid B_2) P(B_2)}$$
                            </div>
                            <div class="formula-desc">Inverts conditional probability: updates prior belief $P(B_1)$ into posterior belief $P(B_1 \mid A)$ upon observing evidence $A$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Machine 1 makes 70% of parts (1% defect); Machine 2 makes 30% (4% defect). If a part is defective, find $P(M_1 \mid D)$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $P(M_1 \\mid D) = \\frac{0.01 \\times 0.70}{(0.01)(0.70) + (0.04)(0.30)} = \\frac{0.007}{0.007 + 0.012} = \\frac{0.007}{0.019} \\approx 0.3684$ (36.84%).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> State the Law of Total Probability for a 2-event partition $\{B, B^c\}$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $P(A) = P(A \\mid B)P(B) + P(A \\mid B^c)P(B^c)$. Total probability decomposes $A$ into mutually exclusive disjoint components.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Sampling Distribution of Sample Variance</span>
                                <span class="nav-badge">Chi-Square</span>
                            </div>
                            <div class="formula-math">
                                $$\\frac{(n - 1) s^2}{\\sigma^2} \\sim \\chi^2_{n - 1}$$
                            </div>
                            <div class="formula-desc">Scaled sample variance of normally distributed data follows a Chi-Square distribution with $n-1$ degrees of freedom.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> For a normal sample with $n = 16$, what is the expected value of $\\frac{(n-1)s^2}{\sigma^2}$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Degrees of freedom $\\nu = n - 1 = 15$. For any $\\chi^2_\\nu$ distribution, $E[\\chi^2_\\nu] = \\nu$. Thus expected value is $15$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What is the variance of the statistic $\\frac{(n-1)s^2}{\\sigma^2}$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{Var}(\\chi^2_\\nu) = 2\\nu = 2(n - 1)$. For $n = 16$, variance $= 2(15) = 30$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Hypergeometric Sampling (Without Replacement)</span>
                                <span class="nav-badge">Combinatorics</span>
                            </div>
                            <div class="formula-math">
                                $$P(X = k) = \\frac{\\binom{K}{k} \\binom{N - K}{n - k}}{\\binom{N}{n}}$$
                            </div>
                            <div class="formula-desc">Probability of $k$ successes in $n$ dependent draws from finite population size $N$ containing $K$ total successes without replacement.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> A lot of 10 items has 3 defectives. If 2 items are drawn without replacement, find $P(X = 2)$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $P(X = 2) = \\frac{\\binom{3}{2}\\binom{7}{0}}{\\binom{10}{2}} = \\frac{3 \\times 1}{45} = \\frac{1}{15} \\approx 0.0667$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> How does this contrast with sampling with replacement?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> With replacement, draws are independent: $P(X = 2) = (3/10) \\times (3/10) = 0.090$ (governed by Binomial distribution $B(n=2, p=0.3)$).</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 3: Essential R Functions Reference Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 3. Essential R Statistical Functions</h3>
                    <div class="table-responsive">
                        <table class="academic-table">
                            <thead>
                                <tr>
                                    <th>Function / Syntax</th>
                                    <th>Signature &amp; Arguments</th>
                                    <th>Description &amp; Operation</th>
                                    <th>Practical Example</th>
                                    <th>Output / Return Value</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="code-cell">mean()</span></td>
                                    <td><code class="inline-code">mean(x, na.rm = FALSE)</code></td>
                                    <td>Calculates arithmetic mean $\\bar{X}$ of numeric vector.</td>
                                    <td><code class="inline-code">mean(c(1, 3, 5, 7, 9))</code></td>
                                    <td><code class="inline-code">5</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">var()</span></td>
                                    <td><code class="inline-code">var(x, na.rm = FALSE)</code></td>
                                    <td>Computes sample variance $s^2$ using denominator $n-1$.</td>
                                    <td><code class="inline-code">var(c(1, 3, 5, 7, 9))</code></td>
                                    <td><code class="inline-code">10</code> (sample variance)</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">sd()</span></td>
                                    <td><code class="inline-code">sd(x)</code></td>
                                    <td>Computes sample standard deviation $s = \\sqrt{s^2}$.</td>
                                    <td><code class="inline-code">sd(c(1, 3, 5, 7, 9))</code></td>
                                    <td><code class="inline-code">3.162278</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">cov() / cor()</span></td>
                                    <td><code class="inline-code">cov(x, y), cor(x, y)</code></td>
                                    <td>Computes sample covariance or Pearson correlation coefficient.</td>
                                    <td><code class="inline-code">cor(c(1,2,3), c(2,4,6))</code></td>
                                    <td><code class="inline-code">1</code> (perfect positive correlation)</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">pnorm()</span></td>
                                    <td><code class="inline-code">pnorm(q, mean=0, sd=1, lower.tail=T)</code></td>
                                    <td>Normal CDF $P(X \\le q)$. Used to compute p-values for Z-tests.</td>
                                    <td><code class="inline-code">2 * (1 - pnorm(1.96))</code></td>
                                    <td><code class="inline-code">0.049996</code> ($\\approx 0.05$)</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">qnorm()</span></td>
                                    <td><code class="inline-code">qnorm(p, mean=0, sd=1)</code></td>
                                    <td>Quantile function of normal distribution (inverse CDF).</td>
                                    <td><code class="inline-code">qnorm(0.975)</code></td>
                                    <td><code class="inline-code">1.959964</code> ($\\approx 1.96$)</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">dnorm()</span></td>
                                    <td><code class="inline-code">dnorm(x, mean=0, sd=1)</code></td>
                                    <td>Normal probability density function $f(x)$ height.</td>
                                    <td><code class="inline-code">dnorm(0)</code></td>
                                    <td><code class="inline-code">0.3989423</code> ($1/\\sqrt{2\\pi}$)</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">t.test()</span></td>
                                    <td><code class="inline-code">t.test(x, y, paired = FALSE, var.equal = FALSE)</code></td>
                                    <td>Performs one-sample, independent two-sample, or paired $t$-test.</td>
                                    <td><code class="inline-code">t.test(after, before, paired = TRUE)</code></td>
                                    <td>$t$-statistic, df, p-value, 95% CI of mean difference</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">chisq.test()</span></td>
                                    <td><code class="inline-code">chisq.test(x, y, p)</code></td>
                                    <td>Performs Pearson's Chi-squared test of independence or goodness-of-fit.</td>
                                    <td><code class="inline-code">chisq.test(table(cat1, cat2))</code></td>
                                    <td>$\\chi^2$ statistic, df, and p-value</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">prop.test()</span></td>
                                    <td><code class="inline-code">prop.test(x, n, p)</code></td>
                                    <td>Tests for null proportion(s) using normal approximation.</td>
                                    <td><code class="inline-code">prop.test(45, 100, p = 0.5)</code></td>
                                    <td>$\\chi^2$ / $Z^2$ statistic, p-value, and confidence interval</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">dhyper() / phyper()</span></td>
                                    <td><code class="inline-code">dhyper(x, m, n, k)</code></td>
                                    <td>Hypergeometric density (without replacement) with $m$ successes, $n$ failures, sample size $k$.</td>
                                    <td><code class="inline-code">dhyper(2, 3, 7, 2)</code></td>
                                    <td>Exact probability ($0.066667$)</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- Section 4: Topic-Wise Example Questions with Solutions -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 4. Topic-Wise Example Questions with Solutions</h3>

                    <!-- Question 1 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Variance of Discrete Uniform Distribution</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 1:</strong> Sumit wants to contact a friend but remembers only the first 9 of the 10 digits. He is certain the last digit is an odd number. He selects one odd digit randomly. If the random variable $X$ denotes the chosen digit, calculate $\\text{Var}(X)$.</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $5$</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> $8$</li>
                                <li><span class="opt-bullet">C.</span> $33$</li>
                                <li><span class="opt-bullet">D.</span> None of the above</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Identify the Support and Probabilities</div>
                                    <p>The possible odd digits are $X \\in \\{1, 3, 5, 7, 9\\}$. Since one digit is chosen randomly, each has equal probability $P(X = x) = \\frac{1}{5}$.</p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Calculate Expected Value $E[X]$</div>
                                    <p>$$E[X] = \\sum x P(X = x) = \\frac{1 + 3 + 5 + 7 + 9}{5} = \\frac{25}{5} = 5$$</p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 3: Calculate Second Moment $E[X^2]$</div>
                                    <p>$$E[X^2] = \\sum x^2 P(X = x) = \\frac{1^2 + 3^2 + 5^2 + 7^2 + 9^2}{5} = \\frac{1 + 9 + 25 + 49 + 81}{5} = \\frac{165}{5} = 33$$</p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 4: Compute Variance</div>
                                    <p>$$\\text{Var}(X) = E[X^2] - (E[X])^2 = 33 - 5^2 = 33 - 25 = 8$$</p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option B (8)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 2 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Variance of Independent Linear Combination</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 2:</strong> Let $X$ and $Y$ be two independent random variables with $\\text{Var}(X) = 9$ and $\\text{Var}(Y) = 3$. Find the variance of the linear combination $Z = 4X - 2Y + 5$.</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $132$</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> $156$</li>
                                <li><span class="opt-bullet">C.</span> $161$</li>
                                <li><span class="opt-bullet">D.</span> $138$</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Apply Variance Operator Rules</div>
                                    <p>By properties of variance for independent random variables:
                                    $$\\text{Var}(aX + bY + c) = a^2\\text{Var}(X) + b^2\\text{Var}(Y) + \\text{Var}(c)$$
                                    Since $5$ is a constant, $\\text{Var}(5) = 0$.
                                    $$\\text{Var}(4X - 2Y + 5) = 4^2 \\text{Var}(X) + (-2)^2 \\text{Var}(Y)$$
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Substitute Given Values</div>
                                    <p>
                                    $$\\text{Var}(4X - 2Y + 5) = 16(9) + 4(3) = 144 + 12 = 156$$
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option B (156)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 3 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Hypothesis Testing Rejection Criterion</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 3:</strong> In hypothesis testing, under what condition will you reject the null hypothesis $H_0$?</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> When the p-value is greater than the significance level $\\alpha$.</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> When the p-value is less than the significance level $\\alpha$.</li>
                                <li><span class="opt-bullet">C.</span> When the p-value is equal to $1$.</li>
                                <li><span class="opt-bullet">D.</span> When the test statistic is zero.</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Statistical Decision Rule</div>
                                    <p>
                                        The significance level $\\alpha$ represents the maximum allowable threshold for Type I error (probability of falsely rejecting a true $H_0$). The p-value quantifies the probability of obtaining data at least as extreme as observed, assuming $H_0$ holds.
                                        <br>• If $\\mathbf{p\\text{-value} &lt; \\alpha}$: The observed data is too improbable under $H_0$. We have statistically significant evidence to <strong>reject $H_0$</strong>.
                                        <br>• If $\\mathbf{p\\text{-value} \\ge \\alpha}$: Insufficient evidence to reject $H_0$. We <strong>fail to reject $H_0$</strong>.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option B (p-value less than $\\alpha$)
                                </div>
                            </div>
                        </details>
                    </div>
                </section>

                <!-- Section 5: Dedicated Assignment-Style Practice Question -->
                <section class="section-block">
                    <div class="assignment-showcase">
                        <div class="assignment-banner">
                            <span>📝 DEDICATED ASSIGNMENT-STYLE PRACTICE CHALLENGE</span>
                            <span>Week 3 Comprehensive</span>
                        </div>
                        <div style="padding: 22px 24px;">
                            <p style="font-weight: 600; font-size: 1rem; color: var(--primary-navy); margin-bottom: 8px;">
                                Problem Statement: One-Sample Z-Test &amp; Significance Inference
                            </p>
                            <p>
                                A manufacturing engineer measures the tensile strength of composite material samples. Theoretical design specifications dictate a nominal mean tensile strength $\\mu = 4.0\\text{ MPa}$. It is known from historical quality audits that the population variance is $\\sigma^2 = 4.0$ (i.e. $\\sigma = 2.0$).
                                <br>A quality assurance team draws $n = 20$ independent and identically distributed (iid) samples, obtaining an observed sample mean tensile strength of:
                                $$\\bar{X} = 5.2\\text{ MPa}$$
                            </p>
                            <ol style="margin-left: 20px; line-height: 1.7; font-size: 0.93rem; margin-top: 10px;">
                                <li>Formulate the null hypothesis $H_0$ and the two-sided alternative hypothesis $H_a$.</li>
                                <li>Calculate the standard error $\\text{SE}(\\bar{X})$ of the sample mean.</li>
                                <li>Compute the test statistic $Z$.</li>
                                <li>At a significance level $\\alpha = 0.05$ (critical value $Z_{0.025} = 1.96$), what conclusion should the test reach? Compute the two-tailed p-value and write the verification R code.</li>
                            </ol>

                            <details class="solution-drawer" style="margin-top: 18px;">
                                <summary><span>📘 View Comprehensive Step-by-Step Instructor Solution</span><span>▼</span></summary>
                                <div class="solution-content">
                                    <div class="step-block">
                                        <div class="step-title">Step 1: Formulate Hypotheses</div>
                                        <p>
                                            Null Hypothesis: $H_0: \\mu = 4.0$ (The true mean tensile strength is $4.0$).
                                            <br>Alternative Hypothesis: $H_a: \\mu \\ne 4.0$ (The true mean tensile strength deviates from $4.0$).
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 2: Calculate Standard Error</div>
                                        <p>
                                            Given $\\sigma = \\sqrt{4} = 2.0$ and $n = 20$:
                                            $$\\text{SE}(\\bar{X}) = \\frac{\\sigma}{\\sqrt{n}} = \\frac{2.0}{\\sqrt{20}} = \\frac{2.0}{4.472136} \\approx 0.447214$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 3: Compute the Z-Statistic</div>
                                        <p>
                                            $$Z = \\frac{\\bar{X} - \\mu_0}{\\text{SE}(\\bar{X})} = \\frac{5.2 - 4.0}{0.447214} = \\frac{1.2}{0.447214} \\approx 2.68328$$
                                            Rounding to two decimal places gives $Z \\approx 2.68$.
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 4: Statistical Decision &amp; p-value Computation</div>
                                        <p>
                                            <strong>Critical Value Comparison:</strong>
                                            For a two-tailed test at $\\alpha = 0.05$, the critical threshold is $Z_{\\text{crit}} = 1.96$.
                                            Since $|Z| = 2.683 &gt; 1.96$, the test statistic falls deep inside the rejection region.
                                            <br><strong>Two-Tailed p-value:</strong>
                                            $$p\\text{-value} = 2 \\times P(Z \\ge 2.683) = 2 \\times [1 - \\Phi(2.683)] \\approx 2 \\times [1 - 0.99635] = 2 \\times 0.00365 = 0.0073$$
                                            Since $p\\text{-value} = 0.0073 &lt; \\alpha = 0.05$, we <strong>reject the null hypothesis $H_0$</strong>. There is statistically significant evidence that the mean tensile strength differs from 4.0 MPa.
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 5: Verification in R</div>
                                        <pre class="r-code"># Given Parameters
mu_0 &lt;- 4.0
sigma &lt;- 2.0
n &lt;- 20
x_bar &lt;- 5.2

# Test Statistic Calculation
se &lt;- sigma / sqrt(n)
z_stat &lt;- (x_bar - mu_0) / se
p_val &lt;- 2 * (1 - pnorm(abs(z_stat)))

cat("Standard Error:", round(se, 4), "\\n")   # 0.4472
cat("Z-Statistic:", round(z_stat, 4), "\\n")    # 2.6833
cat("Two-tailed p-value:", round(p_val, 4), "\\n") # 0.0073
cat("Reject H0 at alpha=0.05?", p_val &lt; 0.05, "\\n") # TRUE</pre>
                                    </div>

                                    <div class="final-answer-box">
                                        ✓ Conclusion: Z = 2.683, p-value = 0.0073. Reject H0; the true mean differs significantly from 4.0.
                                    </div>
                                </div>
                            </details>
                        </div>
                    </div>
                </section>
            </div>
        </article>
        <div class="page-break"></div>
"""

print("Week 3 module loaded.")
