# -*- coding: utf-8 -*-
"""Week 5 Module: Multivariate & Constrained Optimization"""

def get_week5_content():
    return """
        <!-- ============================================================ -->
        <!-- WEEK 5 MODULE -->
        <!-- ============================================================ -->
        <article class="week-module" id="week5">
            <header class="module-header">
                <div class="module-title-group">
                    <h2><span class="module-pill">Week 05</span> Multivariate &amp; Constrained Optimization</h2>
                    <div class="module-lectures">NPTEL Lectures 24–28 | Gradients, Contours, Hessian Matrix, Gradient Descent, Lagrange Multipliers, and KKT Conditions</div>
                </div>
            </header>

            <div class="module-body">
                <!-- Section 1: Core Concepts -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 1. Core Concepts &amp; Systematic Breakdown</h3>
                    <p>
                        Engineering and machine learning systems operate in multidimensional vector spaces $\\mathbb{R}^n$. Multivariate optimization provides the analytical and numerical framework to navigate high-dimensional cost surfaces, find optimal parameter vectors, and satisfy real-world operational constraints.
                    </p>

                    <div style="margin-top: 14px;">
                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">A. Multivariate Differential Calculus: Gradient &amp; Contours</h4>
                        <p>
                            For a scalar field $f(x): \\mathbb{R}^n \\to \\mathbb{R}$, where $x = [x_1, x_2, \\dots, x_n]^T$:
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Gradient Vector $\\nabla f(x)$:</strong> The vector of first-order partial derivatives:
                                $$\\nabla f(x) = \\begin{bmatrix} \\frac{\\partial f}{\\partial x_1} \\ \\frac{\\partial f}{\\partial x_2} \\ \\vdots \\ \\frac{\\partial f}{\\partial x_n} \\end{bmatrix} \\in \\mathbb{R}^{n \\times 1}$$
                            </li>
                            <li><strong>Four Fundamental Geometric Properties of the Gradient:</strong>
                                <ul style="margin-left: 18px; margin-top: 4px;">
                                    <li>1. $\\mathbf{\\nabla f(x)}$ points in the direction of the <strong>greatest (steepest) rate of increase</strong> of the function.</li>
                                    <li>2. $\\mathbf{-\\nabla f(x)}$ points in the direction of the <strong>greatest (steepest) rate of decrease</strong> of the function.</li>
                                    <li>3. The magnitude $\\|\\nabla f(x)\\|$ represents the maximum directional derivative at that point.</li>
                                    <li>4. $\\mathbf{\\nabla f(x)}$ is ALWAYS <strong>orthogonal (perpendicular)</strong> to the contour curves / level sets $f(x) = c$. <em>(Exam Trap: It is NEVER parallel to the contours!)</em></li>
                                </ul>
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">B. The Hessian Matrix, Sylvester's Criterion &amp; Curvature Classification</h4>
                        <p>
                            The second-order curvature of $f(x)$ is captured by the <strong>Hessian matrix</strong> $\\nabla^2 f(x) = H(x) \\in \\mathbb{R}^{n \\times n}$:
                            $$H(x) = \\begin{bmatrix}
                            \\frac{\\partial^2 f}{\\partial x_1^2} &amp; \\frac{\\partial^2 f}{\\partial x_1 \\partial x_2} &amp; \\dots &amp; \\frac{\\partial^2 f}{\\partial x_1 \\partial x_n} \\\\
                            \\frac{\\partial^2 f}{\\partial x_2 \\partial x_1} &amp; \\frac{\\partial^2 f}{\\partial x_2^2} &amp; \\dots &amp; \\frac{\\partial^2 f}{\\partial x_2 \\partial x_n} \\\\
                            \\vdots &amp; \\vdots &amp; \\ddots &amp; \\vdots \\\\
                            \\frac{\\partial^2 f}{\\partial x_n \\partial x_1} &amp; \\frac{\\partial^2 f}{\\partial x_n \\partial x_2} &amp; \\dots &amp; \\frac{\\partial^2 f}{\\partial x_n^2}
                            \\end{bmatrix}$$
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Symmetry Theorem:</strong> By Schwarz's theorem on mixed partials, if second derivatives are continuous, $\\frac{\\partial^2 f}{\\partial x_i \\partial x_j} = \\frac{\\partial^2 f}{\\partial x_j \\partial x_i}$. Therefore, <strong>the Hessian matrix is ALWAYS symmetric ($H = H^T$)</strong>!</li>
                            <li><strong>General Eigenvalue Classification at Stationary Point ($\\nabla f(x^*) = 0$):</strong>
                                <br>• <strong>Strict Local Minimum:</strong> Positive Definite ($H \\succ 0$) $\\iff$ all eigenvalues $\\lambda_i &gt; 0$.
                                <br>• <strong>Strict Local Maximum:</strong> Negative Definite ($H \\prec 0$) $\\iff$ all eigenvalues $\\lambda_i &lt; 0$.
                                <br>• <strong>Saddle Point:</strong> Indefinite $\\iff$ eigenvalues have mixed signs (at least one $\\lambda_i &gt; 0$ and one $\\lambda_j &lt; 0$).
                                <br>• <strong>Inconclusive:</strong> Semi-definite with $\\lambda_i = 0$.
                            </li>
                            <li><strong>2D Sylvester's Determinant Criterion (Crucial Shortcut):</strong>
                                For a 2-variable function with Hessian $H = \\begin{bmatrix} a &amp; b \\\\ b &amp; c \\end{bmatrix} = \\begin{bmatrix} f_{xx} &amp; f_{xy} \\\\ f_{xy} &amp; f_{yy} \\end{bmatrix}$:
                                <br>• $\\det(H) = ac - b^2 &gt; 0$ and $a &gt; 0 \\implies$ <strong>Local Minimum</strong>.
                                <br>• $\\det(H) = ac - b^2 &gt; 0$ and $a &lt; 0 \\implies$ <strong>Local Maximum</strong>.
                                <br>• $\\det(H) = ac - b^2 &lt; 0 \\implies$ <strong>Saddle Point</strong> (eigenvalues have opposite signs).
                                <br>• $\\det(H) = ac - b^2 = 0 \\implies$ Test is <strong>inconclusive</strong>.
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">C. Multidimensional Search Algorithms: Direction &amp; Step Length</h4>
                        <p>
                            All gradient-based iterative optimization algorithms follow the general descent paradigm:
                            $$x_{k+1} = x_k + \\alpha_k d_k$$
                            where at every iteration $k$, the algorithm computes:
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>1. Search Direction $d_k$:</strong> A vector in $\\mathbb{R}^n$ along which the objective function decreases (descent direction satisfies $\\nabla f(x_k)^T d_k &lt; 0$).
                                <br>• In <em>Steepest Descent</em>: $d_k = -\\nabla f(x_k)$.
                                <br>• In <em>Newton's Method</em>: $d_k = -[H(x_k)]^{-1} \\nabla f(x_k)$.
                            </li>
                            <li><strong>2. Step Length $\\alpha_k &gt; 0$:</strong> Determines how far to advance along direction $d_k$ (e.g. constant learning rate, exact line search $\\alpha_k = \\arg\\min_\\alpha f(x_k + \\alpha d_k)$, or backtracking Armijo conditions).
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">D. Constrained Optimization: Direct Substitution vs Lagrange Multipliers</h4>
                        <p>
                            Consider minimizing $f(x_1, x_2)$ subject to an equality constraint $g(x_1, x_2) = 0$:
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li><strong>Direct Substitution Method:</strong> If $g(x_1, x_2) = 0$ can be solved explicitly for one variable (e.g., $x_2 = h(x_1)$), substitute directly into $f(x_1, h(x_1))$ to convert the problem into an unconstrained univariate optimization problem. Simple, but only feasible for algebraically invertible constraints.</li>
                            <li><strong>Lagrange Multipliers (General Analytical Method):</strong>
                                At a constrained optimum, the contour of $f(x)$ must be tangent to the constraint manifold $g(x) = 0$, requiring their gradients to be collinear:
                                $$\\nabla f(x) + \\lambda \\nabla g(x) = 0$$
                                Define the Lagrangian: $L(x, \\lambda) = f(x) + \\lambda g(x)$.
                                <br>Setting $\\nabla_x L = 0$ and $\\frac{\\partial L}{\\partial \\lambda} = g(x) = 0$ yields a system of $n + 1$ equations in $n + 1$ unknowns.
                            </li>
                            <li><strong>Multi-Constraint Lagrangian:</strong> For $m$ equality constraints $g_i(x) = 0$ and $p$ inequality constraints $h_j(x) \\le 0$:
                                $$L(x, \\lambda, \\mu) = f(x) + \\sum_{i=1}^m \\lambda_i g_i(x) + \\sum_{j=1}^p \\mu_j h_j(x)$$
                            </li>
                        </ul>

                        <h4 style="font-size: 1rem; color: var(--secondary-navy); margin-bottom: 6px;">E. Karush–Kuhn–Tucker (KKT) Conditions for Inequalities</h4>
                        <p>
                            For $\\min f(x)$ subject to inequality constraints $h_j(x) \\le 0$ ($j = 1, \\dots, p$):
                            <br>The <strong>KKT Necessary Conditions</strong> at optimum $x^*$ require:
                        </p>
                        <ul style="margin: 8px 0 14px 22px; font-size: 0.92rem;">
                            <li>1. <strong>Stationarity:</strong> $\\nabla f(x^*) + \\sum_{j=1}^p \\mu_j \\nabla h_j(x^*) = 0$</li>
                            <li>2. <strong>Primal Feasibility:</strong> $h_j(x^*) \\le 0$ for all $j$</li>
                            <li>3. <strong>Dual Feasibility:</strong> $\\mu_j \\ge 0$ for all $j$ (non-negative multiplier for $\\le$ inequality)</li>
                            <li>4. <strong>Complementary Slackness:</strong> $\\mu_j h_j(x^*) = 0$ for all $j$. (If constraint is inactive $h_j &lt; 0$, then $\\mu_j = 0$; if active $h_j = 0$, $\\mu_j \\ge 0$).</li>
                        </ul>
                    </div>

                    <!-- Callout: Exam Traps -->
                    <div class="callout-card callout-trap">
                        <div class="callout-icon">⚠️</div>
                        <div class="callout-content">
                            <h4>NPTEL Exam Pitfall: Contour Alignment &amp; Hessian Symmetry</h4>
                            <p>
                                <strong>Statement 1:</strong> <em>"The gradient of a function at a point is parallel to the contours."</em> $\\implies$ <strong>FALSE!</strong> The gradient is strictly perpendicular (orthogonal) to contours.
                                <br><strong>Statement 2:</strong> <em>"Hessian is a non-symmetric matrix."</em> $\\implies$ <strong>FALSE!</strong> For any twice continuously differentiable function, $H = H^T$ is always symmetric.
                                <br><strong>Statement 3:</strong> <em>"The solution to an unconstrained optimization problem is always the same as the constrained one."</em> $\\implies$ <strong>FALSE!</strong> Constraints restrict the feasible domain, typically increasing the minimum cost.
                            </p>
                        </div>
                    </div>

                    <!-- Callout: Professor's Solving Strategy -->
                    <div class="callout-card callout-strategy">
                        <div class="callout-icon">🎯</div>
                        <div class="callout-content">
                            <h4>Professor's 5-Step Lagrange Multiplier Blueprint</h4>
                            <p>
                                When solving $\\min f(x_1, x_2)$ subject to $a x_1 + b x_2 = c$:
                                <br>1. Set up Lagrangian: $L(x_1, x_2, \\lambda) = f(x_1, x_2) + \\lambda(a x_1 + b x_2 - c)$.
                                <br>2. Differentiate w.r.t. $x_1$: $\\frac{\\partial L}{\\partial x_1} = 0 \\implies$ express $x_1$ in terms of $\\lambda$.
                                <br>3. Differentiate w.r.t. $x_2$: $\\frac{\\partial L}{\\partial x_2} = 0 \\implies$ express $x_2$ in terms of $\\lambda$.
                                <br>4. Substitute $x_1(\\lambda)$ and $x_2(\\lambda)$ into constraint $g(x_1, x_2) = 0$ to solve for scalar $\\lambda^*$.
                                <br>5. Back-substitute $\\lambda^*$ to obtain $(x_1^*, x_2^*)$ and evaluate $f(x_1^*, x_2^*)$.
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
                                <span>Multivariate Gradient Vector</span>
                                <span class="nav-badge">Ascent Direction</span>
                            </div>
                            <div class="formula-math">
                                $$\\nabla f(x) = \\left[\\frac{\\partial f}{\\partial x_1}, \\dots, \\frac{\\partial f}{\\partial x_n}\\right]^T$$
                            </div>
                            <div class="formula-desc">Orthogonal to contours; points in direction of steepest ascent. Negative gradient $-\\nabla f$ is steepest descent direction.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Compute $\\nabla f(1, 2)$ for $f(x, y) = 3x^2 y - 4y^3 + 5x$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\frac{\\partial f}{\\partial x} = 6xy + 5 = 6(1)(2) + 5 = 17$; $\\frac{\\partial f}{\\partial y} = 3x^2 - 12y^2 = 3(1) - 12(4) = -45$. Thus $\\nabla f(1, 2) = [17, -45]^T$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What is the geometric relationship between $\\nabla f(x_0)$ and the level curve $f(x) = c$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> The gradient $\\nabla f(x_0)$ is strictly perpendicular (normal) to the contour tangent hyperplane, pointing in the direction of maximum rate of increase.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Hessian Matrix Definiteness</span>
                                <span class="nav-badge">Curvature</span>
                            </div>
                            <div class="formula-math">
                                $$\\lambda_i(H) &gt; 0 \\;\\forall i \\implies \\min, \\quad \\lambda_i(H) &lt; 0 \\;\\forall i \\implies \\max$$
                            </div>
                            <div class="formula-desc">All positive eigenvalues $\implies$ positive definite (local minimum). All negative eigenvalues $\implies$ negative definite (local maximum). Mixed signs $\implies$ saddle point.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> At a stationary point, $H = \\begin{bmatrix} 4 &amp; 1 \\\\ 1 &amp; 3 \\end{bmatrix}$. Classify this point.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\text{tr}(H) = 7 &gt; 0$ and $\\det(H) = 4(3) - 1(1) = 11 &gt; 0$. Both eigenvalues are positive ($H \\succ 0$). Strict local minimum.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If a 2D Hessian has $\\det(H) &lt; 0$ at stationary point $x^*$, what is $x^*$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> In 2D, $\\det(H) = \\lambda_1 \\lambda_2 &lt; 0$ implies one positive and one negative eigenvalue (indefinite). The stationary point is a saddle point.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Lagrangian Stationarity System</span>
                                <span class="nav-badge">Equality Constrained</span>
                            </div>
                            <div class="formula-math">
                                $$\\nabla_x L = \\nabla f(x) + \\lambda \\nabla g(x) = 0, \\quad g(x) = 0$$
                            </div>
                            <div class="formula-desc">Ensures alignment of gradients between objective and constraint manifold at feasible boundary point.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Minimize $f(x, y) = x^2 + y^2$ subject to $x + y = 4$. Find optimal $(x^*, y^*)$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\nabla L = [2x + \\lambda, 2y + \\lambda]^T = 0 \\implies x = y$. Substituting into $x + y = 4 \\implies x^* = 2, y^* = 2$ (min value $= 8$).</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What does the optimal Lagrange multiplier $\\lambda^*$ represent physically?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\lambda^*$ measures the rate of change of the optimal cost with respect to constraint relaxation: $\\lambda^* = -\\frac{\\partial f^*}{\\partial c}$ (shadow price).</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>KKT Complementary Slackness</span>
                                <span class="nav-badge">Inequality Constrained</span>
                            </div>
                            <div class="formula-math">
                                $$\\mu_j h_j(x^*) = 0, \\quad \\mu_j \\ge 0, \\quad h_j(x^*) \\le 0$$
                            </div>
                            <div class="formula-desc">Either the constraint is active ($h_j = 0$), or the multiplier vanishes ($\\mu_j = 0$). Multiplier must be non-negative.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> In minimizing $f(x)$ s.t. $h(x) \\le 0$, the constraint is inactive ($h(x^*) &lt; 0$). What is $\\mu^*$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> By complementary slackness $\\mu^* h(x^*) = 0$. Since $h(x^*) \\ne 0$, multiplier must be zero: $\\mu^* = 0$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What are the 4 fundamental KKT conditions for inequality-constrained optimization?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> (1) Stationarity: $\\nabla f + \\mu \\nabla h = 0$; (2) Primal Feasibility: $h(x^*) \\le 0$; (3) Dual Feasibility: $\\mu \\ge 0$; (4) Complementary Slackness: $\\mu h(x^*) = 0$.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>2D Sylvester's Hessian Criterion</span>
                                <span class="nav-badge">Curvature Test</span>
                            </div>
                            <div class="formula-math">
                                $$ac - b^2 &gt; 0, \\; a &gt; 0 \\implies \\min; \\quad ac - b^2 &gt; 0, \\; a &lt; 0 \\implies \\max; \\quad ac - b^2 &lt; 0 \\implies \\text{saddle}$$
                            </div>
                            <div class="formula-desc">Instant determinant test for 2-variable functions with Hessian $H = \\begin{bmatrix} a &amp; b \\\\ b &amp; c \\end{bmatrix}$. Bypasses explicit eigenvalue computation.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Classify stationary point of $f(x, y)$ if $H = \\begin{bmatrix} 2 &amp; 1 \\\\ 1 &amp; 4 \\end{bmatrix}$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $a = 2 &gt; 0$ and $\\det(H) = (2)(4) - 1^2 = 7 &gt; 0$. Both principal minors are positive $\\implies H$ is positive definite $\\implies$ local minimum.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> What does $H = \\begin{bmatrix} 1 &amp; 3 \\\\ 3 &amp; 2 \\end{bmatrix}$ indicate about curvature?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> $\\det(H) = (1)(2) - 3^2 = -7 &lt; 0$. In 2D, negative determinant indicates opposite eigenvalue signs (indefinite) $\\implies$ saddle point.</div>
                                </div>
                            </div>
                        </div>

                        <div class="formula-card">
                            <div class="formula-title">
                                <span>Multi-Constraint Lagrangian System</span>
                                <span class="nav-badge">General Optimization</span>
                            </div>
                            <div class="formula-math">
                                $$L(x, \\lambda, \\mu) = f(x) + \\sum_{i=1}^m \\lambda_i g_i(x) + \\sum_{j=1}^p \\mu_j h_j(x)$$
                            </div>
                            <div class="formula-desc">Combines objective function with $m$ equality constraints $g_i(x) = 0$ and $p$ inequality constraints $h_j(x) \\le 0$ into a single master scalar function.</div>
                            <div class="formula-examples">
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 1</span> Write the Lagrangian for $\\min x_1^2 + x_2^2$ s.t. $x_1 + x_2 = 10$ and $x_1 \\ge 0$.</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> Rewrite $x_1 \\ge 0$ as standard form $-x_1 \\le 0$. Lagrangian: $L(x_1, x_2, \\lambda, \\mu) = x_1^2 + x_2^2 + \\lambda(x_1 + x_2 - 10) + \\mu(-x_1)$ with $\\mu \\ge 0$.</div>
                                </div>
                                <div class="formula-example-item">
                                    <div class="formula-example-q"><span class="formula-example-badge">Ex 2</span> If the inequality constraint is inactive at optimum, what is $\\mu^*$?</div>
                                    <div class="formula-example-a"><strong>Sol:</strong> By complementary slackness $\\mu^* h(x^*) = 0$. Since $-x_1^* &lt; 0$, $\\mu^*$ must be zero ($0$), so the inequality does not restrict the gradient balance.</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                <!-- Section 3: Essential R Functions Reference Table -->
                <section class="section-block">
                    <h3 class="section-heading"><span class="badge-indicator"></span> 3. Essential R Multivariate Optimization Functions</h3>
                    <div class="table-responsive">
                        <table class="academic-table">
                            <thead>
                                <tr>
                                    <th>Function / Syntax</th>
                                    <th>Signature &amp; Arguments</th>
                                    <th>Optimization Method &amp; Role</th>
                                    <th>Practical Example</th>
                                    <th>Output / Return Value</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><span class="code-cell">optim()</span></td>
                                    <td><code class="inline-code">optim(par, fn, method = "BFGS")</code></td>
                                    <td>General multivariate unconstrained optimization (Nelder-Mead, BFGS, CG, L-BFGS-B).</td>
                                    <td><code class="inline-code">optim(c(0,0), function(x) x[1]^2 + 4*x[2]^2 - 2*x[1] + 8*x[2])</code></td>
                                    <td>List: <code class="inline-code">$par = c(1, -1)</code>, <code class="inline-code">$value = -5</code></td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">nlminb()</span></td>
                                    <td><code class="inline-code">nlminb(start, objective, lower, upper)</code></td>
                                    <td>Unconstrained and box-constrained optimization using PORT routines.</td>
                                    <td><code class="inline-code">nlminb(c(0,0), fn)</code></td>
                                    <td>List: <code class="inline-code">$par</code>, <code class="inline-code">$objective</code>, convergence code</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">constrOptim()</span></td>
                                    <td><code class="inline-code">constrOptim(theta, f, grad, ui, ci)</code></td>
                                    <td>Linearly constrained optimization with linear inequality constraints ($U_i \\theta - c_i \\ge 0$).</td>
                                    <td><code class="inline-code">constrOptim(c(1,1), f, NULL, ui=rbind(c(1,2)), ci=7)</code></td>
                                    <td>Optimal parameter vector satisfying linear bounds</td>
                                </tr>
                                <tr>
                                    <td><span class="code-cell">eigen()</span></td>
                                    <td><code class="inline-code">eigen(H)$values</code></td>
                                    <td>Computes eigenvalues of Hessian matrix to verify positive definiteness.</td>
                                    <td><code class="inline-code">eigen(matrix(c(2,0,0,8), 2, 2))$values</code></td>
                                    <td><code class="inline-code">c(8, 2)</code> (both &gt; 0 $\implies$ positive definite)</td>
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
                            <span class="q-tag q-tag-concept">Topic: Multivariate Conceptual Truths</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 1:</strong> Which of the following statements is/are <strong>NOT TRUE</strong> with respect to multivariate optimization?</p>
                            <ul style="list-style: none; margin: 8px 0 12px 14px; font-size: 0.91rem;">
                                <li><strong>I:</strong> The gradient of a function at a point is parallel to the contours.</li>
                                <li><strong>II:</strong> Gradient points in the direction of greatest increase of the function.</li>
                                <li><strong>III:</strong> Negative gradient points in the direction of greatest decrease of the function.</li>
                                <li><strong>IV:</strong> Hessian is a non-symmetric matrix.</li>
                            </ul>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> I only</li>
                                <li><span class="opt-bullet">B.</span> II and III</li>
                                <li class="correct-option"><span class="opt-bullet">C.</span> I and IV</li>
                                <li><span class="opt-bullet">D.</span> III and IV</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Evaluation of Each Statement</div>
                                    <p>
                                        • <strong>Statement I:</strong> The gradient $\\nabla f$ is mathematically orthogonal (perpendicular) to the contour lines ($f(x) = c$). Hence, Statement I is <strong>FALSE</strong>.
                                        <br>• <strong>Statement II:</strong> By Cauchy-Schwarz inequality, directional derivative $D_u f = \\nabla f^T u$ is maximized when unit vector $u$ is in direction of $\\nabla f$. Hence, Statement II is <strong>TRUE</strong>.
                                        <br>• <strong>Statement III:</strong> The directional derivative is minimized when $u$ is opposite to $\\nabla f$, i.e. in direction $-\\nabla f$. Hence, Statement III is <strong>TRUE</strong>.
                                        <br>• <strong>Statement IV:</strong> For any $C^2$ function, by Clairaut's theorem, mixed partial derivatives commute: $\\frac{\\partial^2 f}{\\partial x_i \\partial x_j} = \\frac{\\partial^2 f}{\\partial x_j \\partial x_i}$. Thus, $H = H^T$ is symmetric. Statement IV is <strong>FALSE</strong>.
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option C (Statements I and IV are NOT TRUE)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 2 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Unconstrained Multivariate Extrema</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 2:</strong> Consider the quadratic objective function:
                            $$f(x_1, x_2) = x_1^2 + 4x_2^2 - 2x_1 + 8x_2$$
                            Find the stationary point, the eigenvalues of the Hessian matrix, and the minimum value of $f$.</p>
                            <ul class="options-list">
                                <li class="correct-option"><span class="opt-bullet">A.</span> Stationary point: $(1, -1)$; Hessian eigenvalues: $2, 8$; Minimum value: $-5$</li>
                                <li><span class="opt-bullet">B.</span> Stationary point: $(-1, 1)$; Hessian eigenvalues: $1, 4$; Minimum value: $0$</li>
                                <li><span class="opt-bullet">C.</span> Stationary point: $(1, -1)$; Hessian eigenvalues: $2, 4$; Minimum value: $-1$</li>
                                <li><span class="opt-bullet">D.</span> Stationary point: $(0, 0)$; Hessian eigenvalues: $2, 8$; Minimum value: $0$</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Compute Gradient and Stationary Point</div>
                                    <p>$$\\frac{\\partial f}{\\partial x_1} = 2x_1 - 2 = 0 \\implies x_1^* = 1$$
                                    $$\\frac{\\partial f}{\\partial x_2} = 8x_2 + 8 = 0 \\implies x_2^* = -1$$
                                    Stationary point is $\\mathbf{(x_1^*, x_2^*) = (1, -1)}$.
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Construct Hessian and Find Eigenvalues</div>
                                    <p>$$H = \\begin{bmatrix}
                                    \\frac{\\partial^2 f}{\\partial x_1^2} &amp; \\frac{\\partial^2 f}{\\partial x_1 \\partial x_2} \\
                                    \\frac{\\partial^2 f}{\\partial x_2 \\partial x_1} &amp; \\frac{\\partial^2 f}{\\partial x_2^2}
                                    \\end{bmatrix} = \\begin{bmatrix} 2 &amp; 0 \\ 0 &amp; 8 \\end{bmatrix}$$
                                    Since $H$ is diagonal, its eigenvalues are simply the diagonal entries:
                                    $$\\mathbf{\\lambda_1 = 2, \\quad \\lambda_2 = 8}$$
                                    Since both eigenvalues are strictly positive ($\\lambda_1 &gt; 0, \\lambda_2 &gt; 0$), $H$ is positive definite, confirming a <strong>strict global minimum</strong>.
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 3: Evaluate Minimum Function Value</div>
                                    <p>$$f(1, -1) = (1)^2 + 4(-1)^2 - 2(1) + 8(-1) = 1 + 4(1) - 2 - 8 = 1 + 4 - 2 - 8 = \\mathbf{-5}$$</p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option A (Stationary: (1, -1), Eigenvalues: 2, 8, Minimum: -5)
                                </div>
                            </div>
                        </details>
                    </div>

                    <!-- Question 3 -->
                    <div class="question-card">
                        <div class="question-header">
                            <span class="q-tag q-tag-calc">Topic: Equality Constrained Optimization</span>
                            <span style="font-size: 0.8rem; color: var(--text-muted);">NPTEL Core Standard</span>
                        </div>
                        <div class="question-body">
                            <p><strong>Question 3:</strong> What is the minimum value of $f(x_1, x_2) = x_1^2 + 4x_2^2 - 2x_1 + 8x_2$ subject to the equality constraint $x_1 + 2x_2 = 7$?</p>
                            <ul class="options-list">
                                <li><span class="opt-bullet">A.</span> $-5$</li>
                                <li><span class="opt-bullet">B.</span> $-1$</li>
                                <li><span class="opt-bullet">C.</span> $15$</li>
                                <li class="correct-option"><span class="opt-bullet">D.</span> $27$</li>
                            </ul>
                        </div>
                        <details class="solution-drawer">
                            <summary><span>💡 View Step-by-Step Instructor Solution</span><span>▼</span></summary>
                            <div class="solution-content">
                                <div class="step-block">
                                    <div class="step-title">Step 1: Formulate the Lagrangian</div>
                                    <p>$$L(x_1, x_2, \\lambda) = x_1^2 + 4x_2^2 - 2x_1 + 8x_2 + \\lambda(x_1 + 2x_2 - 7)$$</p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 2: Take Partial Derivatives &amp; Equate to Zero</div>
                                    <p>$$\\frac{\\partial L}{\\partial x_1} = 2x_1 - 2 + \\lambda = 0 \\implies x_1 = 1 - \\frac{\\lambda}{2}$$
                                    $$\\frac{\\partial L}{\\partial x_2} = 8x_2 + 8 + 2\\lambda = 0 \\implies 4x_2 + 4 + \\lambda = 0 \\implies x_2 = -1 - \\frac{\\lambda}{4}$$
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 3: Substitute into Constraint</div>
                                    <p>$$x_1 + 2x_2 = 7 \\implies \\left(1 - \\frac{\\lambda}{2}\\right) + 2\\left(-1 - \\frac{\\lambda}{4}\\right) = 7$$
                                    $$1 - \\frac{\\lambda}{2} - 2 - \\frac{\\lambda}{2} = 7 \\implies -1 - \\lambda = 7 \\implies \\mathbf{\\lambda = -8}$$
                                    </p>
                                </div>
                                <div class="step-block">
                                    <div class="step-title">Step 4: Compute Coordinates and Constrained Value</div>
                                    <p>$$x_1^* = 1 - \\frac{-8}{2} = 1 + 4 = \\mathbf{5}$$
                                    $$x_2^* = -1 - \\frac{-8}{4} = -1 + 2 = \\mathbf{1}$$
                                    <em>Check constraint:</em> $x_1 + 2x_2 = 5 + 2(1) = 7$ (satisfied!).
                                    <br>Evaluate objective:
                                    $$f(5, 1) = (5)^2 + 4(1)^2 - 2(5) + 8(1) = 25 + 4 - 10 + 8 = \\mathbf{27}$$
                                    Notice: The constrained minimum ($27$) is much higher than unconstrained minimum ($-5$), as the constraint restricts the domain!
                                    </p>
                                </div>
                                <div class="final-answer-box">
                                    ✓ Correct Answer: Option D (27)
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
                            <span>Week 5 Comprehensive</span>
                        </div>
                        <div style="padding: 22px 24px;">
                            <p style="font-weight: 600; font-size: 1rem; color: var(--primary-navy); margin-bottom: 8px;">
                                Problem Statement: Constrained Maximum of a Paraboloid via Lagrange Multipliers
                            </p>
                            <p>
                                Find the maximum value of the concave paraboloid:
                                $$f(x, y) = 49 - x^2 - y^2$$
                                subject to the linear budget/resource constraint:
                                $$x + 3y = 10$$
                            </p>
                            <ol style="margin-left: 20px; line-height: 1.7; font-size: 0.93rem; margin-top: 10px;">
                                <li>Formulate the Lagrangian function $L(x, y, \\lambda)$ for this constrained problem.</li>
                                <li>Derive the first-order necessary conditions (FONC) with respect to $x$, $y$, and $\\lambda$.</li>
                                <li>Solve the resulting system of linear equations for the optimal coordinates $(x^*, y^*)$ and multiplier $\\lambda^*$.</li>
                                <li>Compute the exact maximum value $f(x^*, y^*)$.</li>
                                <li>Verify the solution using geometric distance principles from the origin to the line $x + 3y = 10$.</li>
                            </ol>

                            <details class="solution-drawer" style="margin-top: 18px;">
                                <summary><span>📘 View Comprehensive Step-by-Step Instructor Solution</span><span>▼</span></summary>
                                <div class="solution-content">
                                    <div class="step-block">
                                        <div class="step-title">Step 1: Formulate the Lagrangian</div>
                                        <p>
                                            We want to maximize $f(x, y)$ subject to $g(x, y) = x + 3y - 10 = 0$:
                                            $$L(x, y, \\lambda) = (49 - x^2 - y^2) - \\lambda(x + 3y - 10)$$
                                            (or equivalently $+ \\lambda(x + 3y - 10)$ with opposite sign of $\\lambda$).
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 2: First-Order Necessary Conditions (FONC)</div>
                                        <p>
                                            $$\\frac{\\partial L}{\\partial x} = -2x - \\lambda = 0 \\implies x = -\\frac{\\lambda}{2}$$
                                            $$\\frac{\\partial L}{\\partial y} = -2y - 3\\lambda = 0 \\implies y = -\\frac{3\\lambda}{2}$$
                                            $$\\frac{\\partial L}{\\partial \\lambda} = -(x + 3y - 10) = 0 \\implies x + 3y = 10$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 3: Solve for $\lambda$ and Optimal Coordinates</div>
                                        <p>
                                            Substitute expressions for $x$ and $y$ into the constraint:
                                            $$\\left(-\\frac{\\lambda}{2}\\right) + 3\\left(-\\frac{3\\lambda}{2}\\right) = 10$$
                                            $$-\\frac{\\lambda}{2} - \\frac{9\\lambda}{2} = 10 \\implies -\\frac{10\\lambda}{2} = 10 \\implies -5\\lambda = 10 \\implies \\mathbf{\\lambda = -2}$$
                                            Now evaluate coordinates:
                                            $$x^* = -\\frac{-2}{2} = \\mathbf{1}$$
                                            $$y^* = -\\frac{3(-2)}{2} = \\mathbf{3}$$
                                            <em>Verification on constraint line:</em> $1 + 3(3) = 1 + 9 = 10$ (exactly satisfied!).
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 4: Compute Maximum Constrained Value</div>
                                        <p>
                                            $$f(1, 3) = 49 - (1)^2 - (3)^2 = 49 - 1 - 9 = \\mathbf{39}$$
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 5: Geometric Verification</div>
                                        <p>
                                            Maximizing $49 - (x^2 + y^2)$ is identical to minimizing the squared Euclidean distance from the origin to the line:
                                            $$d^2 = x^2 + y^2$$
                                            The perpendicular distance from origin $(0, 0)$ to line $Ax + By + C = 0$ ($x + 3y - 10 = 0$) is:
                                            $$d = \\frac{|1(0) + 3(0) - 10|}{\\sqrt{1^2 + 3^2}} = \\frac{10}{\\sqrt{10}} = \\sqrt{10}$$
                                            Therefore, the minimum squared distance is $d^2 = (\\sqrt{10})^2 = 10$.
                                            Substituting into objective: $f_{\\max} = 49 - d^2 = 49 - 10 = \\mathbf{39}$.
                                            The geometric and Lagrangian derivations match with mathematical perfection!
                                        </p>
                                    </div>

                                    <div class="step-block">
                                        <div class="step-title">Step 6: R Code Verification</div>
                                        <pre class="r-code"># Negative objective for minimization
fn &lt;- function(v) -(49 - v[1]^2 - v[2]^2)

# Constraint: x + 3y = 10  =&gt; x = 10 - 3y
# Substitute constraint to convert to 1D unconstrained problem
fn_1d &lt;- function(y) -(49 - (10 - 3*y)^2 - y^2)
opt &lt;- optimize(fn_1d, interval = c(-10, 10))

y_star &lt;- opt$minimum
x_star &lt;- 10 - 3 * y_star
max_val &lt;- -opt$objective

cat(sprintf("Optimal x* = %.4f, y* = %.4f\\n", x_star, y_star)) # x*=1, y*=3
cat(sprintf("Constrained Maximum f(x*, y*) = %.4f\\n", max_val)) # 39.0000</pre>
                                    </div>

                                    <div class="final-answer-box">
                                        ✓ Conclusion: Optimal point (x*, y*) = (1, 3), Lagrange multiplier lambda = -2, Maximum Value = 39.
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

print("Week 5 module loaded.")
