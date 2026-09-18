# -*- coding: utf-8 -*-
"""Week 4 Module: Optimization Foundations & Univariate Methods"""

def get_week4_content():
    return """
        <!-- ============================================================ -->
        <!-- WEEK 4 MODULE -->
        <!-- ============================================================ -->
        <article class="week-module" id="week4">
            <header class="module-header">
                <div class="module-title-group">
                    <h2><span class="module-pill">Week 04</span> Optimization Foundations: Univariate Methods</h2>
                    <div class="module-lectures">NPTEL Lectures 23–26 | Problem Formulation, Local vs Global Extrema, FONC/SOSC, Convexity, and Iterative Search</div>
                </div>
            </header>

            <div class="module-body">
                <!-- Section 1: Core Concepts -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 1. Core Concepts &amp; Systematic Breakdown</h3>
                    <p>
                        Machine learning and data science can be unified as applied optimization problems. Whether finding best-fit linear regression parameters by minimizing squared errors, maximizing classification likelihoods, or minimizing cluster variances, optimization provides the mathematical engine.
                    </p>

                    <div style="margin-top: 14px;">
                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">A. Mathematical Optimization Problem Formulation</h4>
                        <p>
                            A mathematical optimization model is formally defined by three elements:
                            $$\\min_{x \\in \\Omega} f(x) \\quad \\text{or} \\quad \\max_{x \\in \\Omega} f(x)$$
                            where $f(x): \\mathbb{R} \\to \\mathbb{R}$ is the <strong>objective function</strong>, $x$ is the <strong>decision variable</strong>, and $\\Omega \\subseteq \\mathbb{R}$ is the <strong>feasible region</strong> bounded by operational equality ($h_i(x) = 0$) and inequality ($g_j(x) \\le 0$) constraints.
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Optimization Duality (Sign Inversion):</strong> Maximizing $f(x)$ is mathematically identical to minimizing $-f(x)$:
                                $$\\max_{x \\in \\Omega} f(x) \\iff \\min_{x \\in \\Omega} [-f(x)]$$
                            </li>
                            <li><strong>Global vs Local Extrema:</strong>
                                <br>• $x^*$ is a <em>global minimum</em> if $f(x^*) \\le f(x)$ for all $x \\in \\Omega$.
                                <br>• $x^*$ is a <em>local minimum</em> if $f(x^*) \\le f(x)$ in an $\\epsilon$-neighborhood around $x^*$.
                            </li>
                            <li><strong>Extreme Value Theorem (Weierstrass):</strong> If $f(x)$ is continuous on a <em>closed and bounded interval</em> $[a, b]$, $f(x)$ is guaranteed to attain both an absolute maximum and an absolute minimum on $[a, b]$.
                                <br>• <strong>CRITICAL SOLVING PROCEDURE:</strong> Evaluate $f(x)$ at:
                                <br>&nbsp;&nbsp;&nbsp;&nbsp;1. All interior stationary points $x_i \\in (a, b)$ where $f'(x_i) = 0$.
                                <br>&nbsp;&nbsp;&nbsp;&nbsp;2. All points where $f'(x)$ fails to exist.
                                <br>&nbsp;&nbsp;&nbsp;&nbsp;3. <strong>The interval boundary endpoints $x = a$ and $x = b$!</strong>
                                <br>The largest of these candidate values is the global maximum; the smallest is the global minimum.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">B. Analytical Optimality Conditions (FONC &amp; SOSC)</h4>
                        <p>For a continuous, twice-differentiable univariate function $f(x)$ on an open domain:</p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>First-Order Necessary Condition (FONC):</strong>
                                <br>If $x^*$ is an interior local extremum, the first derivative must vanish:
                                $$\\mathbf{f'(x^*) = 0}$$
                                Points where $f'(x^*) = 0$ are called <strong>stationary points</strong>.
                            </li>
                            <li><strong>Second-Order Necessary Condition (SONC):</strong>
                                <br>• If $x^*$ is a local minimum $\\implies f''(x^*) \\ge 0$.
                                <br>• If $x^*$ is a local maximum $\\implies f''(x^*) \\le 0$.
                            </li>
                            <li><strong>Second-Order Sufficient Condition (SOSC):</strong>
                                <br>Let $x^*$ be a stationary point ($f'(x^*) = 0$):
                                <br>• $\\mathbf{f''(x^*) &gt; 0} \\implies x^*$ is a <strong>strict local minimum</strong> (curving upward).
                                <br>• $\\mathbf{f''(x^*) &lt; 0} \\implies x^*$ is a <strong>strict local maximum</strong> (curving downward).
                                <br>• $\\mathbf{f''(x^*) = 0} \\implies$ Inconclusive (test higher derivatives).
                            </li>
                            <li><strong>Higher-Order Derivative Rule (Inflection Points):</strong>
                                If the first non-vanishing derivative at a stationary point is of <em>odd order</em> $k$ (e.g. $f'''(x^*) \\ne 0$), then $x^*$ is an <strong>inflection point</strong> (neither min nor max, e.g. $f(x) = x^3$ at $0$). If of <em>even order</em> $k$, it is a min if $f^{(k)}(x^*) &gt; 0$ and max if $f^{(k)}(x^*) &lt; 0$ (e.g. $f(x) = x^4$ at $0$).
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">C. Convexity and Uniqueness of Optima</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Convex Function:</strong> A function $f(x)$ is convex if $f''(x) \\ge 0$ everywhere on the interval.
                                <br><strong>Fundamental Convexity Theorem:</strong> For a convex function, <em>any local minimum is unconditionally a global minimum</em>! If $f''(x) &gt; 0$ strictly, the global minimum is unique.
                            </li>
                            <li><strong>Concave Function:</strong> $f''(x) \\le 0$ everywhere. Any local maximum is a global maximum.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">D. Numerical Univariate Search Methods (Bracketing &amp; Interpolation)</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Bisection Method (Derivative-Based):</strong> Used to solve $f'(x) = 0$ inside bracketing interval $[a, b]$ where $f'(a) f'(b) &lt; 0$.
                                <br>• At each iteration, evaluates midpoint $m = (a + b)/2$ and discards half the interval.
                                <br>• Interval width after $k$ steps: $\\Delta_k = \\frac{b - a}{2^k}$.
                                <br>• <strong>Linear convergence</strong> with error reduction factor $1/2$. Guaranteed convergence, though slow.
                            </li>
                            <li><strong>Golden Section Search (Derivative-Free):</strong> Finds minimum of unimodal $f(x)$ on $[a, b]$ without computing derivatives.
                                <br>• Maintains constant golden ratio $\\tau = \\frac{\\sqrt{5} - 1}{2} \\approx 0.618$. Discards $1 - \\tau \\approx 0.382$ of the interval each step.
                            </li>
                            <li><strong>Secant Method:</strong> Replaces the exact second derivative $f''(x_k)$ in Newton's method with a finite difference slope between two successive points $x_k, x_{k-1}$:
                                $$x_{k+1} = x_k - f'(x_k) \\frac{x_k - x_{k-1}}{f'(x_k) - f'(x_{k-1})}$$
                                Exhibits <strong>superlinear convergence</strong> (order $\\approx 1.618$) without requiring $f''(x)$.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">E. Gradient Descent &amp; Newton–Raphson</h4>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Gradient Descent (1D):</strong> Steps opposite to the local slope:
                                $$x_{k+1} = x_k - \\alpha f'(x_k)$$
                                where $\\alpha &gt; 0$ is the learning rate (step size). If $\\alpha$ is too small, convergence is sluggish; if $\\alpha$ is too large, it overshoots and diverges.
                            </li>
                            <li><strong>Newton–Raphson Method for Optimization:</strong> Minimizes local 2nd-order Taylor expansion:
                                $$x_{k+1} = x_k - \\frac{f'(x_k)}{f''(x_k)}$$
                                Exhibits <strong>quadratic convergence</strong> ($|e_{k+1}| \\propto |e_k|^2$) near the optimum. Requires $f''(x_k) &gt; 0$.
                            </li>
                        </ul>
                    </div>

                    <!-- Callout: Exam Traps -->
                    <div class="callout-card callout-trap">
                        <div class="callout-icon">⚠️</div>
                        <div class="callout-content">
                            <h4>NPTEL Exam Pitfall: Root-Finding vs Optimization in Newton-Raphson</h4>
                            <p>
                                <strong>Common Blunder:</strong> Students frequently mix up the two distinct forms of Newton-Raphson:
                                <br>1. Finding roots of $g(x) = 0$: $x_{k+1} = x_k - \\frac{g(x_k)}{g'(x_k)}$.
                                <br>2. Minimizing/Maximizing $f(x)$: We seek roots of $f'(x) = 0$, hence: $x_{k+1} = x_k - \\frac{\\mathbf{f'(x_k)}}{\\mathbf{f''(x_k)}}$.
                                <br>Remember: Optimization requires the ratio of the <strong>first derivative</strong> over the <strong>second derivative</strong>!
                            </p>
                        </div>
                    </div>

                    <!-- Callout: Professor's Solving Strategy -->
                    <div class="callout-card callout-strategy">
                        <div class="callout-icon">🎯</div>
                        <div class="callout-content">
                            <h4>Professor's 4-Step Polynomial Extrema Protocol</h4>
                            <p>
                                Given $f(x) = ax^3 + bx^2 + cx + d$:
                                <br>1. Compute $f'(x) = 3ax^2 + 2bx + c$.
                                <br>2. Set $f'(x) = 0$ and solve quadratic equation: $x^* = \\frac{-2b \\pm \\sqrt{4b^2 - 12ac}}{6a}$.
                                <br>3. Compute $f''(x) = 6ax + 2b$.
                                <br>4. Substitute each root into $f''(x^*)$: If positive $\\implies$ local min; if negative $\\implies$ local max.
                            </p>
                        </div>
                    </div>
                </section>

                <!-- Section 2: Formatted Formulas & Rules Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 2. Essential Mathematical Formulas &amp; Conditions</h3>
                    <div class="formula-grid">
                        <div class="formula-card">
                            <div class="formula-title">
                                <span>FONC (First Order Necessary)</span>
                                <span class="nav-badge">Stationarity</span>
                            </div>
                            <div class="formula-math">
                                $$f'(x^*) = 0$$
                            </div>
                            <div class="formula-desc">Slope of tangent line vanishes at interior local extrema. Identifies all candidate stationary points.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Find candidate stationary points for $f(x) = 2x^3 - 9x^2 + 12x - 5$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Set $f'(x) = 6x^2 - 18x + 12 = 0 \\implies 6(x-1)(x-2) = 0$. Candidate points are $x_1^* = 1$ and $x_2^* = 2$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Is $x^* = 0$ a local extremum for $f(x) = x^3$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $f'(0) = 0$ satisfies FONC, but $f''(0) = 0$ and $f(x)$ changes sign across $0$ (inflection point). FONC is necessary but not sufficient.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>SOSC (Second Order Sufficient)</span>
                                <span class="nav-badge">Curvature</span>
                            </div>
                            <div class="formula-math">
                                $$f''(x^*) &gt; 0 \\implies \\min, \\quad f''(x^*) &lt; 0 \\implies \\max$$
                            </div>
                            <div class="formula-desc">Positive curvature indicates a strictly convex valley (minimum). Negative curvature indicates a concave peak (maximum).</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Classify stationary points $x = 1$ and $x = 2$ for $f(x) = 2x^3 - 9x^2 + 12x - 5$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $f''(x) = 12x - 18$. At $x = 1$: $f''(1) = -6 &lt; 0 \\implies$ local maximum. At $x = 2$: $f''(2) = +6 &gt; 0 \\implies$ local minimum.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> For $f(x) = e^x + e^{-x}$, find the nature of the stationary point at $x^* = 0$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $f'(0) = e^0 - e^0 = 0$. Curvature $f''(x) = e^x + e^{-x} &gt; 0 \\; \\forall x$. At $x^*=0$, $f''(0) = 2 &gt; 0 \\implies$ strictly convex global minimum ($f(0) = 2$).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Newton-Raphson Optimization Step</span>
                                <span class="nav-badge">Algorithm</span>
                            </div>
                            <div class="formula-math">
                                $$x_{k+1} = x_k - \\frac{f'(x_k)}{f''(x_k)}$$
                            </div>
                            <div class="formula-desc">Second-order iterative step using local curvature to locate stationary points with quadratic convergence speed.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Minimize $f(x) = x^4 - 4x + 1$ with $x_0 = 2$. Compute $x_1$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $f'(x) = 4x^3 - 4$, $f''(x) = 12x^2$. At $x_0 = 2$: $f'(2) = 28$, $f''(2) = 48$. Step: $x_1 = 2 - 28/48 = 1.4167$ (rapidly approaching root $x^* = 1$).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> When does Newton-Raphson optimization break down?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> It fails when $f''(x_k) = 0$ (division by zero / zero curvature) or when initiated where $f''(x_k) &lt; 0$ (diverges toward a maximum).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Taylor Series (2nd Order)</span>
                                <span class="nav-badge">Approximation</span>
                            </div>
                            <div class="formula-math">
                                $$f(x) \\approx f(x_0) + f'(x_0)(x - x_0) + \\frac{1}{2}f''(x_0)(x - x_0)^2$$
                            </div>
                            <div class="formula-desc">Local quadratic model approximating any smooth function around expansion point $x_0$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Write the 2nd-order Taylor approximation of $f(x) = \\ln(x)$ around $x_0 = 1$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $f(1) = 0, f'(1) = 1, f''(1) = -1$. Approximation: $f(x) \\approx (x - 1) - \\frac{1}{2}(x - 1)^2$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> Estimate $\\cos(0.2)$ using quadratic Taylor expansion around $x_0 = 0$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\cos(x) \\approx 1 - \\frac{1}{2}x^2$. For $x = 0.2$: $1 - 0.5(0.04) = 0.98$ (exact is $\\approx 0.980067$).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Bisection Interval Halving Bound</span>
                                <span class="nav-badge">Bracketing</span>
                            </div>
                            <div class="formula-math">
                                $$\\Delta_k = \\frac{b - a}{2^k} \\le \\epsilon \\implies k \\ge \\frac{\\ln((b - a)/\\epsilon)}{\\ln 2}$$
                            </div>
                            <div class="formula-desc">Guarantees error reduction by factor of 2 per iteration. Calculates minimum iterations $k$ required to achieve tolerance $\epsilon$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Given initial bracket $[1, 5]$ and target tolerance $\epsilon = 0.05$, find the minimum iterations $k$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\Delta_k = (5 - 1)/2^k = 4/2^k \\le 0.05 \\implies 2^k \\ge 80$. Since $2^6 = 64$ and $2^7 = 128$, minimum $k = 7$ iterations.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What is the asymptotic rate and order of convergence of Bisection?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Order of convergence is 1 (linear), with asymptotic error constant $C = 1/2$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Gradient Descent Univariate Step</span>
                                <span class="nav-badge">Descent Search</span>
                            </div>
                            <div class="formula-math">
                                $$x_{k+1} = x_k - \\alpha f'(x_k)$$
                            </div>
                            <div class="formula-desc">Iteratively updates position opposite to the local derivative slope with step size (learning rate) $\\alpha &gt; 0$.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> For $f(x) = x^2 - 4x + 4$, step size $\\alpha = 0.1$, and start $x_0 = 0$, compute $x_1$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Derivative $f'(x) = 2x - 4$. At $x_0 = 0$: $f'(0) = -4$. Step: $x_1 = 0 - 0.1(-4) = +0.4$ (moves closer to optimum $x^* = 2$).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What happens if $\\alpha = 1.0$ when minimizing $f(x) = x^2$ from $x_0 = 3$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $f'(x) = 2x$. $x_1 = 3 - 1.0(6) = -3$; $x_2 = -3 - 1.0(-6) = +3$. The iterates oscillate indefinitely between $+3$ and $-3$ without converging.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 3: Essential R Functions Reference Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 3. Essential R Optimization Functions</h3>
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
                                    <td><span class="code-cell">optimize()</span></td>
                                    <td><code class="inline-code">optimize(f, interval, maximum = FALSE)</code></td>
                                    <td>Golden-section search with parabolic interpolation for 1D functions.</td>
                                    <td><code class="inline-code">optimize(function(x) x^2 - 4*x, c(-5, 5))</code></td>
                                    <td>List: <code class="inline-code">$minimum = 2</code>, <code class="inline-code">$objective = -4</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">D()</span></td>
                                    <td><code class="inline-code">D(expr, name)</code></td>
                                    <td>Symbolic differentiation of mathematical expression.</td>
                                    <td><code class="inline-code">D(expression(x^3 + 6*x^2), "x")</code></td>
                                    <td><code class="inline-code">3 * x^2 + 6 * (2 * x)</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">deriv()</span></td>
                                    <td><code class="inline-code">deriv(expr, name, func = TRUE)</code></td>
                                    <td>Computes symbolic derivative and returns an executable R function with gradient.</td>
                                    <td><code class="inline-code">df &lt;- deriv(~ x^2 - 2*x, "x", func=T)</code></td>
                                    <td>Function evaluating value and gradient at $x$</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">uniroot()</span></td>
                                    <td><code class="inline-code">uniroot(f, interval)</code></td>
                                    <td>Finds root $f(x) = 0$ in an interval where sign change occurs.</td>
                                    <td><code class="inline-code">uniroot(function(x) 2*x - 4, c(0, 5))</code></td>
                                    <td>List: <code class="inline-code">$root = 2</code></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                <!-- Section 4: Topic-Wise Example Questions with Solutions -->
                <section class="section-block" id="week4-practice">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 4. Topic-Wise Example Questions with Solutions</h3>

                    <!-- Question 1 -->
                    <div class="question-card filter-item filter-mcq">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Stationary Points &amp; Extrema of Cubic Polynomial</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 1:</strong> Let $f(x) = x^3 + 6x^2 - 3x - 5$. Select all correct options from the following:</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $-2 + \\sqrt{5}$ will give the maximum for $f(x)$.</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> $-2 + \\sqrt{5}$ will give the minimum for $f(x)$.</li>
                                <li class="correct-option"><span class="opt-bullet">C.</span> The stationary points for $f(x)$ are $-2 + \\sqrt{5}$ and $-2 - \\sqrt{5}$.</li>
                                <li><span class="opt-bullet">D.</span> The stationary points for $f(x)$ are $-4$ and $0$.</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Compute First Derivative (FONC)</div>
                                    <p>Given $f(x) = x^3 + 6x^2 - 3x - 5$:
                                    $$f'(x) = 3x^2 + 12x - 3$$
                                    Set $f'(x) = 0$:
                                    $$3x^2 + 12x - 3 = 0 \\iff x^2 + 4x - 1 = 0$$
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Solve for Stationary Points</div>
                                    <p>Using the quadratic formula $x = \\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}$:
                                    $$x = \\frac{-4 \\pm \\sqrt{4^2 - 4(1)(-1)}}{2(1)} = \\frac{-4 \\pm \\sqrt{16 + 4}}{2} = \\frac{-4 \\pm \\sqrt{20}}{2} = \\frac{-4 \\pm 2\\sqrt{5}}{2} = -2 \\pm \\sqrt{5}$$
                                    Thus, the stationary points are $x_1 = -2 + \\sqrt{5} \\approx 0.236$ and $x_2 = -2 - \\sqrt{5} \\approx -4.236$. (Confirms Option C).
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 3: Evaluate Second Derivative (SOSC)</div>
                                    <p>$$f''(x) = 6x + 12$$
                                    <br>• For $x_1 = -2 + \\sqrt{5}$:
                                    $$f''(-2 + \\sqrt{5}) = 6(-2 + \\sqrt{5}) + 12 = -12 + 6\\sqrt{5} + 12 = 6\\sqrt{5} &gt; 0$$
                                    Since $f''(-2 + \\sqrt{5}) &gt; 0$, $x = -2 + \\sqrt{5}$ corresponds to a <strong>local minimum</strong>. (Confirms Option B).
                                    <br>• For $x_2 = -2 - \\sqrt{5}$:
                                    $$f''(-2 - \\sqrt{5}) = 6(-2 - \\sqrt{5}) + 12 = -6\\sqrt{5} &lt; 0 \\implies \\text{local maximum}.$$
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answers: Options B and C
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 2 -->
                    <div class="question-card filter-item filter-mcq">
                        <div class="question-header">
                            <span class="q-tag q-tag-concept">Topic: Second-Order Sufficient Condition</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 2:</strong> What is the second-order sufficient condition for $x^*$ to be a strict local maximizer of the function $f(x)$?</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $f''(x^*) &gt; 0$</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> $f''(x^*) &lt; 0$</li>
                                <li><span class="opt-bullet">C.</span> $f''(x^*) = 0$</li>
                                <li><span class="opt-bullet">D.</span> $f'(x^*) &gt; 0$</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Mathematical Theory</div>
                                    <p>
                                        At a stationary point where $f'(x^*) = 0$:
                                        <br>• If $f''(x^*) &lt; 0$, the slope is strictly decreasing through $x^*$, meaning the function transitions from increasing to decreasing. The curve is concave downward, guaranteeing a strict local maximum.
                                        <br>• Conversely, $f''(x^*) &gt; 0$ guarantees a strict local minimum.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option B ($f''(x^*) < 0$)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 3 -->
                    <div class="question-card filter-item filter-mcq">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Extrema of Trigonometric Function</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 3:</strong> Let $f(x) = 2\\sin x$ for $0 \\le x \\le 2\\pi$. Which of the following statements are correct? (Select all that apply.)</p>
                            <ul class="options-list">
                                <li class="correct-option"><span class="opt-bullet">A.</span> $x = \\pi/2$ gives a local maximum for $f(x)$.</li>
                                <li class="correct-option"><span class="opt-bullet">B.</span> $x = 3\\pi/2$ gives a local minimum for $f(x)$.</li>
                                <li><span class="opt-bullet">C.</span> $x = \\pi$ is a stationary point.</li>
                                <li><span class="opt-bullet">D.</span> The maximum value of $f(x)$ is $1$.</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Differentiate and Find Critical Points</div>
                                    <p>$$f'(x) = 2\\cos x = 0 \\implies x = \\frac{\\pi}{2}, \\quad x = \\frac{3\\pi}{2} \\quad \\text{in } [0, 2\\pi]$$</p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Second Derivative Test</div>
                                    <p>$$f''(x) = -2\\sin x$$
                                    <br>• At $x = \\pi/2$: $f''(\\pi/2) = -2\\sin(\\pi/2) = -2 &lt; 0 \\implies$ Local Maximum with value $f(\\pi/2) = 2(1) = 2$.
                                    <br>• At $x = 3\\pi/2$: $f''(3\\pi/2) = -2\\sin(3\\pi/2) = -2(-1) = 2 &gt; 0 \\implies$ Local Minimum with value $f(3\\pi/2) = 2(-1) = -2$.
                                    <br>• At $x = \\pi$: $f'(\\pi) = 2\\cos(\\pi) = -2 \\ne 0$, so $\\pi$ is NOT a stationary point.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answers: Options A and B
                                </div>
                            </div>
                        </details>
                    </div>
                </section>

                <!-- Section 5: Dedicated Assignment-Style Practice Question -->
                <section class="section-block">
                    <div class="assignment-showcase filter-item filter-assignment">
                        <div class="assignment-banner">
                            <span>📝 DEDICATED ASSIGNMENT-STYLE PRACTICE CHALLENGE</span>
                            <span>Week 4 Comprehensive</span>
                        </div>
                        <div style="padding: 22px 24px;">
                            <p style="font-weight: 600; font-size: 1rem; color: var(--primary-navy); margin-bottom: 8px;">
                                Problem Statement: Newton-Raphson Iterative Optimization &amp; Convergence
                            </p>
                            <p>
                                Consider the non-linear cost function:
                                $$f(x) = x^3 + 6x^2 - 3x - 5$$
                                An engineer seeks to locate the local minimum $x^*$ numerically using the <strong>Newton-Raphson optimization algorithm</strong> starting from an initial estimate of $x_0 = 0$.
                            </p>
                            <ol style="margin-left: 20px; line-height: 1.7; font-size: 0.93rem; margin-top: 10px;">
                                <li>State the exact analytic expression for the Newton-Raphson optimization update formula $x_{k+1} = g(x_k)$.</li>
                                <li>Manually compute the first iteration value $x_1$ starting from $x_0 = 0$.</li>
                                <li>Manually compute the second iteration value $x_2$.</li>
                                <li>Compare $x_2$ with the exact analytical local minimum $x^* = -2 + \\sqrt{5} \\approx 0.236068$ and calculate the absolute error $|x_2 - x^*|$.</li>
                                <li>Write R code to implement 5 iterations of this algorithm.</li>
                            </ol>

                            <details class="solution-drawer" style="margin-top: 18px;">
                                <summary><span>📘 View Comprehensive Step-by-Step Instructor Solution</span><span>▼</span></summary>
                                <div class="solution-content">
                                    <div class="step-block">
                                        <div class="step-title">Step 1: Newton-Raphson Update Formula</div>
                                        <p>
                                            We minimize $f(x)$ by finding the root of $f'(x) = 0$:
                                            $$f'(x) = 3x^2 + 12x - 3, \\quad f''(x) = 6x + 12$$
                                            The general Newton-Raphson update is:
                                            $$x_{k+1} = x_k - \\frac{f'(x_k)}{f''(x_k)} = x_k - \\frac{3x_k^2 + 12x_k - 3}{6x_k + 12}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 2: Iteration 1 ($k = 0$, $x_0 = 0$)</div>
                                        <p>
                                            $$f'(0) = 3(0)^2 + 12(0) - 3 = -3$$
                                            $$f''(0) = 6(0) + 12 = 12$$
                                            $$x_1 = 0 - \\frac{-3}{12} = 0 - (-0.25) = \\mathbf{0.25}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 3: Iteration 2 ($k = 1$, $x_1 = 0.25$)</div>
                                        <p>
                                            $$f'(0.25) = 3(0.25)^2 + 12(0.25) - 3 = 3(0.0625) + 3 - 3 = 0.1875$$
                                            $$f''(0.25) = 6(0.25) + 12 = 1.5 + 12 = 13.5$$
                                            $$x_2 = 0.25 - \\frac{0.1875}{13.5} = 0.25 - 0.013889 = \\mathbf{0.236111}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 4: Error Comparison</div>
                                        <p>
                                            Exact analytical minimum: $x^* = -2 + \\sqrt{5} \\approx 0.23606798$.
                                            <br>Absolute error after only 2 iterations:
                                            $$|x_2 - x^*| = |0.23611111 - 0.23606798| = 0.00004313 \\approx 4.31 \\times 10^{-5}$$
                                            This illustrates the rapid quadratic convergence of the Newton-Raphson scheme!
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 5: R Code Simulation</div>
                                        <pre class="r-code"># Define functions
f_prime &lt;- function(x) 3*x^2 + 12*x - 3
f_double &lt;- function(x) 6*x + 12

# Newton-Raphson Solver
x &lt;- 0 # Initial guess x0
cat(sprintf("Iter 0: x = %.6f\\n", x))

for (iter in 1:4) {
  x &lt;- x - f_prime(x) / f_double(x)
  cat(sprintf("Iter %d: x = %.8f | Error = %.2e\\n", iter, x, abs(x - (-2 + sqrt(5)))))
}</pre>
                                    </div>

                                    <div class="final-answer-box">
                                        ✓ Results: x1 = 0.25, x2 = 0.236111; converges to x* = -2 + sqrt(5) within 2 iterations.
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

print("Week 4 module loaded.")
